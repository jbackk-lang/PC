# MODEL_PC_TIMDR — Rdzeń TIMDER na strukturze F4‑RED (252 stany)

## 1. Założenia modelu

PC (Processing Core) nie jest klasycznym CPU binarnym.  
Model PC_TIMDR zakłada:

- przestrzeń stanów zbudowaną na figurze **F4 z redukcją jednego ramienia (F4‑RED)**,  
- **9 pierwiastków strukturalnych** (ΔS, τ, Λ × 3 ramiona), każdy w stanie \(\pm 1\),  
- warunek równowagi:



\[
|N_{+} - N_{-}| \le 1
\]



co daje dokładnie:



\[
\binom{9}{4} + \binom{9}{5} = 126 + 126 = 252
\]



PC pracuje **wyłącznie** w tej przestrzeni 252 dopuszczalnych konfiguracji.

---

## 2. Przestrzeń stanów i adresacja 256‑bit

Każdy stan rdzenia PC:

- jest reprezentowany jako **wektor 9 wartości \(\pm 1\)**,  
- jest interpretowany jako obiekt `F4State` (moduł `filter_252.py`),  
- przechodzi przez filtr `F4Filter252`, który dopuszcza tylko 252 konfiguracje.

Adresacja:

- przestrzeń adresowa: \(0 \dots 255\) (256 możliwych kodów),  
- 252 kody odpowiadają dopuszczalnym konfiguracjom F4‑RED,  
- 4 kody są zarezerwowane (reset, null, over‑τ, over‑ΔS).

W praktyce:

- **256‑bit** jest nośnikiem adresowym,  
- **252 stany** są rzeczywistą przestrzenią obliczeniową TIMDR.

---

## 3. Warstwa filtrująca — PCFilterLayer

Centralnym elementem modelu jest `PCFilterLayer`:

- przyjmuje wektor 9 × \(\pm 1\),  
- tworzy `F4State`,  
- wywołuje `F4Filter252.apply(state)`,  
- zwraca `True/False` oraz statystyki zaakceptowanych/odrzuconych stanów.

Każdy moduł rdzenia (Motion, Rotation, Twist, Tetroid, Triangle, SkretAI, Memory, JCompressor, TwistOperator):

- generuje nowy stan,  
- natychmiast przepuszcza go przez `PCFilterLayer`,  
- kontynuuje pracę tylko, jeśli stan jest dopuszczalny w F4‑RED.

To gwarantuje, że **cały rdzeń PC działa wyłącznie w przestrzeni 252 stanów**.

---

## 4. Moduły geometryczne rdzenia PC

### Motion

- operator przesunięcia stanu w osi czasu/fazy,  
- metoda `step(state_vector)` generuje nowy stan,  
- wynik jest walidowany przez `PCFilterLayer`.

### Rotation

- operator obrotu w triadzie λ‑τ‑ρ,  
- metoda `rotate(bits)` operuje na 9‑bitowym wektorze,  
- wynik przechodzi przez filtr F4‑RED.

### Twist / TwistOperator

- operator skrętu Möbiusa (He → Fe → Og),  
- metoda `apply(bits)` wykonuje transformację skrętu,  
- wynik jest dopuszczalny tylko, jeśli spełnia warunek 252 konfiguracji.

### Tetroid

- struktura czterowymiarowego stanu geometrycznego,  
- metoda `evolve(bits)` wykonuje ewolucję stanu,  
- każdy krok jest walidowany przez filtr.

### Triangle

- lokalna projekcja skrętu na 2D,  
- metoda `project(bits)` przekształca stan i sprawdza dopuszczalność.

### SkretAI

- warstwa interpretacji pola,  
- metoda `process(bits)` tłumaczy stan na wyższy poziom,  
- działa tylko na stanach dopuszczonych przez F4‑RED.

### Memory (TransitionMemory)

- pamięć przejściowa sekwencji stanów,  
- metoda `push(bits)` zapisuje tylko stany zaakceptowane przez filtr,  
- `get()` zwraca wyłącznie sekwencje zgodne z modelem TIMDR.

### JCompressor

- kompresja strukturalna = **redukcja jednego ramienia**,  
- metoda `compress(JPoint)` wykonuje transformację i walidację F4‑RED,  
- zwraca skompresowany punkt tylko, jeśli stan jest dopuszczalny.

---

## 5. Spójność z MAPA‑PO‑HELU i TIMDR

Model PC_TIMDR jest spójny z:

- **MAPA‑PO‑HELU** — 126 konfiguracji materii + 126 antykonfiguracji,  
- **F4‑RED** — figura z redukcją jednego ramienia, dająca mocniejsze wiązania,  
- **TIMDR/GIA** — interpretacja stanów jako konfiguracje pola, nie klasyczne bity.

PC:

- nie liczy „0/1”,  
- liczy **konfiguracje geometryczne** w przestrzeni 252 stanów,  
- używa 256‑bitowej szerokości jako naturalnej ramy adresowej.

---

## 6. Pipeline TIMDR w PC

Typowy przepływ:



\[
\text{Motion} \rightarrow \text{Rotation} \rightarrow \text{TwistOperator} \rightarrow \text{Tetroid} \rightarrow \text{Triangle} \rightarrow \text{SkretAI} \rightarrow \text{Memory}
\]



Na każdym etapie:

- stan jest reprezentowany jako 9 × \(\pm 1\),  
- przechodzi przez `PCFilterLayer`,  
- jeśli filtr odrzuci stan, pipeline się zatrzymuje,  
- jeśli filtr zaakceptuje stan, przejście jest zapisywane w `TransitionMemory`.

Test integracyjny `test_pipeline_timdr.py` weryfikuje, że:

- pipeline działa,  
- filtr odrzuca część losowych stanów,  
- zaakceptowane stany tworzą spójną sekwencję w przestrzeni F4‑RED.

---

## 7. Cel modelu PC_TIMDR

MODEL_PC_TIMDR definiuje:

- **rdzeń maszyny TIMDER**,  
- pracujący na **252 dopuszczalnych konfiguracjach F4‑RED**,  
- z **256‑bitową przestrzenią adresową**,  
- z pełną integracją filtra dopuszczalności na każdym etapie.

To jest docelowy model:

- dla przyszłego **TIMDR‑CPU**,  
- dla integracji z **MAPA‑PO‑HELU**,  
- dla dalszych rozszerzeń (np. warstwy sieciowe, IO, wizualizacja pola).

PC w tej postaci jest już **spójnym, geometrycznym rdzeniem**, gotowym do dalszego rozwoju w ramach TIMDR.

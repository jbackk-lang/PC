README — PC (Processing Core TIMDER)
Architektura obliczeniowa oparta na strukturze F4‑RED (252 stany)
PC jest rdzeniem obliczeniowym systemu TIMDER.
Nie jest klasycznym procesorem binarnym, lecz maszyną geometryczną pracującą na pełnej strukturze F4 z redukcją jednego ramienia, która daje 252 dopuszczalne stany.
To jest natywna przestrzeń obliczeniowa TIMDR/GIA.

Repozytorium PC zawiera operatory i struktury, które odwzorowują tę geometrię:

Motion — operator przesunięcia w przestrzeni stanów

Rotation — operator obrotu w triadzie λ‑τ‑ρ

Twist — operator skrętu Möbiusa

Tetroid — czterowymiarowy stan geometryczny

Triangle — lokalna projekcja skrętu

Memory — przejściowa pamięć stanów

SkretAI — warstwa interpretacji i translacji pola

JCompressor — kompresja strukturalna (redukcja ramienia)

Całość tworzy przenośny rdzeń TIMDER, który nie liczy bitów, tylko konfiguracje geometryczne.

1. Dlaczego PC pracuje na strukturze 252?
W modelu TIMDR:

figura F4 ma 4 ramiona,

ale jedno ramię jest zredukowane,

trzy ramiona przejmują jego rolę,

sprzężenia J są dociśnięte,

wiązania ΔS‑τ‑Λ są mocniejsze niż w klasycznej F4.

Każde z trzech aktywnych ramion generuje:

ΔS — zero entropii

τ — zero fazy czasu

Λ — zero stabilizacji

Łącznie:

3
 ramiona
×
3
 pierwiastki
=
9
Każdy pierwiastek ma dwa stany sprzężenia:

(
+
)
,
  
(
−
)
Pełna liczba konfiguracji:

2
9
=
512
Warunek równowagi F4‑RED:

∣
𝑁
+
−
𝑁
−
∣
≤
1
Dopuszczalne konfiguracje:

(
9
4
)
+
(
9
5
)
=
126
+
126
=
252
To jest pełna przestrzeń obliczeniowa TIMDR.

2. Dlaczego PC musi być 256‑bitowy?
Struktura 252 stanów wymaga przestrzeni adresowej:

0
–
255
256 = 
2
8

252 mieści się w niej idealnie, a 4 stany pozostają jako:

reset

null

over‑τ

over‑ΔS

Dlatego PC nie może być:

64‑bit

128‑bit

192‑bit

Pierwsza szerokość, która pozwala odwzorować pełną F4‑RED, to 256‑bit.

PC jest więc procesorem geometrycznym, który:

nie operuje na bitach,

operuje na 252‑stanowej strukturze F4‑RED,

a 256‑bitowa szerokość jest tylko nośnikiem adresowym.

3. Jak moduły PC odwzorowują F4‑RED?
Motion — przesuwa konfigurację wzdłuż osi τ
Rotation — obraca stan w triadzie λ‑τ‑ρ
Twist — wykonuje skręt Möbiusa (He → Fe → Og)
Tetroid — przechowuje pełny stan geometryczny (9 pierwiastków strukturalnych)
Triangle — lokalna projekcja skrętu na 2D
Memory — zapisuje przejścia między konfiguracjami
SkretAI — interpretuje stan jako strukturę pola
JCompressor — wykonuje redukcję ramienia (kluczowe dla F4‑RED)

Każdy moduł jest translatorem geometrycznym, nie klasycznym algorytmem.

4. Powiązanie z MAPA‑PO‑HELU
MAPA‑PO‑HELU rekonstruuje:

126 konfiguracji materii (po He)

126 konfiguracji antymaterii

Razem:

126
+
126
=
252
PC jest rdzeniem, który:

operuje na tej samej przestrzeni,

interpretuje te same stany,

wykonuje ruchy, skręty i rotacje w tej samej geometrii.

Dlatego PC i MAPA‑PO‑HELU są kompatybilne bez żadnych konwersji.

5. Dlaczego wiązania są mocniejsze niż w klasycznej F4?
W klasycznej F4:

4 ramiona,

równomierne sprzężenia,

słabsze wiązania.

W F4‑RED:

jedno ramię jest ściągnięte,

trzy ramiona przejmują jego rolę,

sprzężenia J są dociśnięte,

ΔS‑τ‑Λ są bardziej zwarte,

stabilność lokalna jest większa.

To powoduje:

mocniejsze wiązania,

bardziej stabilne konfiguracje,

wyraźniejszą strukturę 126 + 126.

PC musi odwzorować właśnie tę wersję F4, nie klasyczną.

6. Cel repozytorium PC
Repo PC jest rdzeniem maszyny TIMDER, która:

operuje na 252 stanach F4‑RED,

używa 256‑bitowej przestrzeni adresowej,

wykonuje operacje geometryczne zamiast binarnych,

interpretuje ruch, skręt i rotację jako operacje na polu,

jest kompatybilna z MAPA‑PO‑HELU i math‑validator‑2.0.

To jest fundament przyszłego TIMDR‑komputera.


# tests/test_filter_252.py

import random
from filter_252 import F4State, F4Filter252


def generate_random_state() -> F4State:
    # losowy 9-bitowy stan ±1
    bits = [random.choice([-1, 1]) for _ in range(9)]
    return F4State(bits=bits)


def test_filter_252_distribution():
    """
    Porównawcza walidacja:
    - generujemy dużą liczbę stanów (np. 10_000)
    - przepuszczamy przez filtr F4-RED
    - sprawdzamy, że liczba zaakceptowanych jest ~252 / 512 przestrzeni,
      czyli ok. połowa wszystkich losowych stanów.
    """
    filt = F4Filter252()
    n = 10_000

    for _ in range(n):
        s = generate_random_state()
        filt.filter_state(s)

    stats = filt.stats()
    print("ACCEPTED:", stats["accepted"])
    print("REJECTED:", stats["rejected"])

    # Tu możesz ręcznie porównać z dotychczasowym zachowaniem rdzenia:
    # np. ile stanów Motion/Rotation/Twist generuje poza dopuszczalną przestrzenią.
    assert stats["accepted"] > 0
    assert stats["rejected"] > 0

## ## 8. Kodowanie 252 → 256 (warstwa adresowa TIMDR‑CPU)

Rdzeń TIMDR operuje na 252 dopuszczalnych konfiguracjach F4‑RED.  
Przestrzeń adresowa CPU ma 256 możliwych kodów (0–255).  
Warstwa kodowania 252→256 zapewnia stabilne odwzorowanie:

- 252 stanów geometrycznych,
- 4 stany specjalne (meta‑stany).

### 8.1. Struktura kodowania

Każdy stan F4‑RED jest reprezentowany jako wektor:



\[
v = (b_1, b_2, \dots, b_9),\quad b_i \in \{-1, +1\}
\]



który spełnia warunek równowagi:



\[
|N_{+} - N_{-}| \le 1
\]



Warstwa kodowania przypisuje każdemu dopuszczalnemu stanowi unikalny kod:



\[
\text{encode}(v) \rightarrow k,\quad k \in \{0,1,\dots,251\}
\]



Pozostałe cztery kody są zarezerwowane:

- 252 — RESET  
- 253 — NULL  
- 254 — OVER\_τ  
- 255 — OVER\_ΔS  

### 8.2. Własności kodowania

Kodowanie jest:

- **bijekcją** między 252 stanami F4‑RED a kodami 0–251,
- **stabilne** — każdy stan ma zawsze ten sam kod,
- **odwracalne** — możliwa jest rekonstrukcja stanu:



\[
\text{decode}(k) \rightarrow v
\]



dla każdego \(k 

## 9. State9 — wspólny format stanu TIMDR

State9 jest jednolitym formatem reprezentacji stanu w rdzeniu TIMDR.  
Każdy moduł PC (Motion, Rotation, TwistOperator, Tetroid, Triangle, SkretAI, Memory, JCompressor) operuje na tej samej strukturze:



\[
\text{State9} = (b_1, b_2, \dots, b_9),\quad b_i \in \{-1, +1\}
\]



gdzie dziewięć wartości odpowiada dziewięciu pierwiastkom strukturalnym F4‑RED:

- ΔS  
- τ  
- Λ₁  
- Λ₂  
- Λ₃  
- trzy sprzężenia ramion  
- dwa sprzężenia stabilizujące

State9 jest minimalną, kompletną reprezentacją stanu geometrycznego TIMDR.

### 9.1. Własności State9

State9 spełnia:



\[
|N_{+} - N_{-}| \le 1
\]



co oznacza, że należy do przestrzeni 252 dopuszczalnych konfiguracji F4‑RED.  
Każdy stan jest natychmiast walidowany przez `PCFilterLayer`.

State9 jest:

- **atomowy** — nie ma części opcjonalnych,  
- **geometryczny** — nie jest binarny,  
- **jednolity** — wszystkie moduły PC używają tej samej struktury,  
- **odwracalny** — można go zakodować i odkodować (sekcja 8).

### 9.2. Znaczenie State9 w TIMDR‑CPU

State9 jest tym, czym „słowo maszynowe” jest dla klasycznego CPU.  
W TIM

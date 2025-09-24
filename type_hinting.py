# Any - assegnato automaticamente per i valori non specificati
# non effettua alcun controllo sulla variabili

#-----------------------

# Optional[T] corrisponde a Union[T, None]
# Specifica il tipo di valore ma rimane opzionale

# Union[A, B] specifica i valori che DEVONO essere di tipo A o B

# Optional si usa quando l'alternativa è None
# altrimenti si usa Union
# sintassi Optional --> Optional[tipo elemento]
# sintassi Union --> Union[tipo elemento, tipo elemento]

# --------------------

# list[T], Dict[K, V], Tuple[...], Set[T] 
# collezioni di oggetti esistenti in python, 
# in questo caso parametrizzano gli elementi
# sintassi Tuple[tipo elemento, tipo elemento]
# se tipo omogeneo ma numero indefinito --> Tuple[tipo elemento, ...
# sintassi Dict[tipo elemento, tipo elemento]
# spesso Dict[str, int]

# Callable[[ArgTypes, ..], ReturnType] 
# firma di una funzione, la rende chiamabile
# passare funzioni come parametri ad altre funzioni


# list[str], dict[str, int] per Python 3.9 +
# Tuple --> valori con posizione o ruolo specifici
# Callable --> funzioni di callback

# ----------------------

# Esercizi Type Hinting 

# funzione che somma due interi e ritorna la somma (specifica i type hints)
def somma(a: int, b:int) -> int:
    return a + b

print(somma(3, 2))

# greeting() con stringa opzionale come parametro
# se fornita ritorna "Ciao, stringa!"
# altrimenti "Ciao, ospite!" (usa Optional)
from typing import Optional
def greeting(s: Optional[str] = None) -> str:
    if s:
        return f"Ciao, {s}!"
    
    return "Ciao, ospite!"

print(greeting("Luca"))
print(greeting())

# to_string() accetta int, float 
# ritorna str "Il valore è" (usa Union)
from typing import Union
def to_string(x: Union[int, float]) -> str:
    return f"Il valore è {x}"

print(to_string(3))
print(to_string(5.2))

# applica_due_volte() accetta numero intero e funzione
# richiama due volte la funzione passata come parametro
# ritorna risultato funzione (usa Callable)
from typing import Callable
def applica_due_volte(n: int, funz: Callable[[int], int]) -> int:
    return funz(funz(n))

print(applica_due_volte(2, lambda x: x**2))

# scambia() prende in input valori dello stesso tipo
# ritorna i valori scambiati (usa TypeVar)
from typing import TypeVar
Tipo = TypeVar("Tipo", int, float)
def scambia(a: Tipo, b: Tipo) -> Tipo:
    return b, a

print(scambia(1, 2))

# crea_animale() accetta Classe Animale o sottoclassi
# ritorna un'istanza di essa (usa Type)
from typing import Type
class Animale:
    def verso(self):
        return ""
    
class Mucca(Animale):
    def verso(self):
        return "Moo Moo!"
    
def crea_animale(c: Type[Animale]) -> Animale:
    return c()

print(crea_animale(Mucca).verso())
    
# classe Box generica che accetta valore di qualsiasi tipo
# metodo get_valore che ritorna il valore 
# (usa Generic, TypeVar)
from typing import Generic, TypeVar
T = TypeVar("T")
class Box(Generic[T]):
    def __init__(self, valore: T) -> T:
        self.valore = valore
    
    def get_valore(self) -> T:
        return self.valore

print(Box(3).get_valore())
print(Box("ciao").get_valore())
print(Box(2.5).get_valore())

# media() che accetta lista di numeri int o float
# ritorna media aritmetica 
# (usa Union o TypeVar vincolato in int e float)
from typing import Union, TypeVar, List
Specifico = TypeVar("Specifico", int, float)
def media(l: List[Specifico]) -> float:
    return sum(l) / len(l)

def media1(l: List[Union[int, float]]) -> float:
    return sum(l) / len(l)

print(media([1, 2, 3, 4, 5]))
print(media1([1, 2, 3, 4, 5]))
# METACARATTERI DELLE REGEX

# prende qualsiasi carattere --> .
# prende solo l'inizio della stringa --> ^
# prende solo la fine della stringa --> $
# definisce una classe di caratteri --> [abc] --> prende a, b o c
# definisce una classe NEGATA --> [^abc] --> prende tutto tranne a, b, c
# indica un intervallo dentro le quadre --> [a-z] --> lettere minuscole
# operatore OR (alternativa) --> a|b --> prende "a" oppure "b"
# definisce un gruppo catturante --> ( ... )
# definisce un gruppo NON catturante --> (?: ... )
# definisce un gruppo catturante NOMINATO --> (?P<nome> ...)

# ------------------
# QUANTIFICATORI

# prende 0 o più ripetizioni --> *
# prende 1 o più ripetizioni --> +
# prende 0 o 1 ripetizione --> ?
# indica esattamente un numero --> {n}
# indica ALMENO n volte --> {n,}
# indica da n a m volte --> {n,m}

# ----------------
# CLASSI DI CARATTERI PREDEFINITE

# prende i caratteri delle cifre --> \d --> equivalente di [0-9]
# prende i caratteri delle parole --> \w --> equivalente di [a-zA-Z0-9_]
# prende gli spazi bianchi --> \s --> equivalente di [ \t\n\r\f\v]
# non prende le cifre --> \D --> equivalente di [^0-9]
# non prende i caratteri delle parole --> \W --> equivalente di [^a-zA-Z0-9_]
# non prende gli spazi --> \S --> equivalente di [^ \t\n\r\f\v]
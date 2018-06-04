# TwitterAPI: appunti di utilizzo
Per l'inizializzazione si veda test.py

# Json
Facendo una ricerca per hashtag, si ottiene una risposta (visibile con r.json())

la risposta json è organizzata:

_search_metadata_: contiene le informazioni principali sull'esito della ricerca

_statuses_: lista che comprende l'elenco degli _stati_ che riguardano la/le keyword inserite

            il singolo status è indicizzato
            
_esempio di status_

... in _entities_ si trovano gli _hashtags_ del tweet

... in _user_ si trovano le informazioni dell'utente, es. _screen_name_


il codice sotto stampa i nomi degli utenti

```
for item in r.json()['statuses']:
    print (item['user']['screen_name'])
```    

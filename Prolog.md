# Cwieczenie z wprowadzenia #
% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space

% Your program goes here
kobieta(kasia).
mezczyzna(marek).
lubi(jan, pawel).
lubi(marek, kasia).
lubi(kasia, marek).

przyjazn(X, Y) :-
    lubi(X, Y),
    lubi(Y, X).
niby_przyjazn(X, Y) :-
    lubi(X, Y);
    lubi(Y, X).

loves(X, Y) :-
    lubi(X, Y),
    lubi(Y, X),
    \+lubi(Y, \+X).
/**true_love(X, Y) :-
    lubi(X, Y),
    lubi(Y, X),
    \+lubi(Y, \+X),
    kobieta(X),
    mezczyzna(Y).
    **/
true_love(X, Y) :-
    lubi(X, Y),
    lubi(Y, X),
    \+lubi(Y, \+X),
    (   kobieta(X),
    mezczyzna(Y));
    (   kobieta(Y),
    mezczyzna(X)).

/** <examples> Your example queries go here, e.g.
?- member(X, [cat, mouse]).
*/

# Zadanie 1 #
% Rodzeństwo
rodzenstwo(X, Y) :- rodzic(Z, X), rodzic(Z, Y), X \= Y.

%wujkiem x jest 
%wojtek marek
wujek(X, Y) :- dziadkowie(Z, X), rodzic(Z, Y).


% Bracia
bracia(X, Y) :- rodzic(A, X), rodzic(A, Y), X \= Y.

% Przyrodnie rodzeństwo (mają wspólnych tylko jednego rodzica)
przyrodnie_rodzenstwo(X, Y) :- rodzic(A, X), rodzic(B, Y), A \= B.

% Przybrane rodzeństwo (mają wspólnych obu rodziców)
przybrane_rodzenstwo(X, Y) :- rodzic(A, X), rodzic(A, Y), rodzic(B, X), rodzic(B, Y), A \= B.

% Dziadkowie bronek wojtek
dziadkowie(X, Y) :- rodzic(X, Z), rodzic(Z, Y).

kuzyn(X, Y) :- dziadkowie(A, X), dziadkowie(A, Y), X \= Y.
wnuk(Y, X) :- rodzic(X, Z), rodzic(Z, Y).
% Rodzice
rodzic(ele, michal).
rodzic(janusz, michal).
rodzic(ele, wojtek).
rodzic(janusz, wojtek).
rodzic(bronek, janusz).
rodzic(bronek, marek).


# Zadanie 2 #
kobieta(X) :- \+ mężczyzna(X).
ojciec(X, Y) :- rodzic(X, Y), mężczyzna(X).
matka(X, Y) :- rodzic(X, Y), \+ mężczyzna(X).
córka(X, Y) :- rodzic(X, Y), kobieta(X).
brat_rodzony(X, Y) :- rodzic(Z, X), rodzic(Z, Y), mężczyzna(X), X \= Y.
kuzyn(X, Y) :- dziadek(A, X), dziadek(A, Y), X \= Y.
dziadek_od_strony_ojca(X, Y) :- ojciec(X, Z), ojciec(Z, Y), mężczyzna(X).
dziadek_od_strony_matki(X, Y) :- ojciec(X, Z), matka(Z, Y), kobieta(X).
dziadek(X, Y) :- ojciec(X, Z), rodzic(Z, Y).
babcia(X, Y) :- matka(X, Z), rodzic(Z, Y).
wnuczka(X, Y) :- babcia(Y, X).


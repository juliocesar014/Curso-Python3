update estados
set nome = 'Maranhão'
where sigla = 'MA'

-- pode usar tanto aspas simples ' ' , tanto aspas duplas " "

select nome from estados
where sigla = "MA"


update estados
set nome = 'Paraná', populacao = 11.32
where sigla = 'PR'

select * from estados


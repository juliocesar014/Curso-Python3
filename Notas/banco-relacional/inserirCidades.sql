select * from estados WHERE id = 37

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Campinas', 795, 25)

INSERT INTO cidades (nome,area, estado_id)
VALUES ('Niterói', 133.9, 31 )

select * from cidades

INSERT INTO cidades (nome,area,estado_id)
VALUES ('Caruaru', 920.6,(select id from estados where sigla = 'PE'))

select * from cidades

INSERT INtO cidades (nome,area,estado_id)
VALUES ('Juazeiro', 248.2,(select id from estados WHERE sigla = 'CE'))

select * from cidades
INSERT INTO empresas(nome,cnpj)
VALUES 
    ('Bradesco',08459358000158),
    ('NuBank', 14258413011158),
    ('Cielo', 08402374000155);

ALTER TABLE empresas modify cnpj VARCHAR(20);

select * from empresas

desc empresas;

select * from empresas;
select * from cidades;

INSERT INTO empresas_unidades (empresa_id,cidade_id,sede)
VALUES 
    (1,1,1),
    (1,2,0),
    (2,1,0);

select * from empresas,empresas_unidades
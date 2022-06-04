select e.nome, c.nome
from empresas e, empresas_unidades eu, cidades c
where e.id = eu.empresa_id 
and c.cidade = eu.cidade_id
and sede
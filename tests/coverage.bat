REM    Essa rotina de comandos faz com que seja aberto o arquivo coverage, de modo que podemos ver, de modo 
REM    mais simplificado, a 

pytest tests/ -v --cov=meuapp

coverage html

opera htmlcov/index.html
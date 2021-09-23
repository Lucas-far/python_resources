

def parte_1():
    """
    Ir ao git bash e executar [ ssh-keygen.exe -t rsa ]

    --------------------------- Etapas que acontecem após iniciar a criação de uma chave SSH ---------------------------
    Etapa 1: Enter file in which to save the key        [ pode ser ignorada = ENTER ]
    Etapa 2: Enter passphrase (empty for no passphrase) [ pode ser ignorada = ENTER ]
    Etapa 3: Enter same passphrase again:               [ pode ser ignorada = ENTER ]
    Etapa 4: Your identification has been saved in
    Etapa 5: Your public key has been saved in
    Etapa 6: The key fingerprint is:

    Na etapa 5, ir para o local especifico no Git Bash, abrir o arquivo id_rsa.pub e copiar o seu conteúdo

    ------------------------------------------------ No site do Github ------------------------------------------------
    Avatar -> settings -> ssh and gpg keys -> new ssh key -> preencher nome -> preencher chave com o conteúdo copiado ->
    add ssh key
    """

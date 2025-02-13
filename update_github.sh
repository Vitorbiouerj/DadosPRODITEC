#!/bin/bash

# Nome do repositório remoto e branch principal
REPO_URL="https://github.com/Vitorbiouerj/DadosPRODITEC.git"
BRANCH="main"

# Caminho do arquivo de credenciais
CREDENTIALS_FILE="/IA/github.txt"

# Verifica se o arquivo de credenciais existe e configura o login automático
if [ -f "$CREDENTIALS_FILE" ]; then
    echo "Carregando credenciais do GitHub..."
    GITHUB_USER=$(sed -n '1p' "$CREDENTIALS_FILE")
    GITHUB_TOKEN=$(sed -n '2p' "$CREDENTIALS_FILE")

    # Configura o Git para login automático
    git config --global credential.helper store
    echo "https://$GITHUB_USER:$GITHUB_TOKEN@github.com" > ~/.git-credentials
fi

# Instala e ativa o Git LFS
git lfs install

# Buscar arquivos maiores que 100MB
LARGE_FILES=$(find . -type f -size +100M)

if [ -n "$LARGE_FILES" ]; then
    echo "Os seguintes arquivos excedem 100MB e serão gerenciados pelo Git LFS:"
    echo "$LARGE_FILES"

    # Adicionar arquivos grandes ao Git LFS
    for FILE in $LARGE_FILES; do
        git lfs track "$FILE"
    done

    # Garantir que o .gitattributes seja versionado
    git add .gitattributes
    git commit --allow-empty -m "Configurando Git LFS para arquivos grandes"

    # Migrar arquivos já existentes para o Git LFS
    git lfs migrate import --include="*.ipynb,*.csv,*.html"
fi

# Puxa as atualizações do repositório remoto para evitar conflitos
echo "Sincronizando repositório local com remoto..."
git pull --rebase origin $BRANCH

# Adiciona todos os arquivos ao commit
git add --all

# Solicita a mensagem do commit
echo "Digite a mensagem do commit:"
read COMMIT_MSG

# Cria o commit
git commit -m "$COMMIT_MSG"

# Faz o push usando Git LFS
echo "Fazendo push dos arquivos para o GitHub com Git LFS..."
git push origin $BRANCH

echo "Sincronização concluída com sucesso!"


#!/bin/bash

# Nome do repositório remoto
REPO_URL="https://github.com/Vitorbiouerj/DadosPRODITEC.git"

# Buscar arquivos maiores que 100MB
LARGE_FILES=$(find . -type f -size +100M)

if [ -n "$LARGE_FILES" ]; then
    echo "Os seguintes arquivos excedem 100MB e serão adicionados ao .gitignore:"
    echo "$LARGE_FILES"

    # Adicionar arquivos grandes ao .gitignore
    echo "$LARGE_FILES" >> .gitignore
    sort -u -o .gitignore .gitignore  # Remover duplicatas do .gitignore

    # Garantir que esses arquivos não sejam mais rastreados pelo Git
    git rm --cached $LARGE_FILES 2>/dev/null

    # Criar um commit para registrar a atualização do .gitignore
    git add .gitignore
    git commit -m "Atualizando .gitignore para ignorar arquivos grandes"
fi

# Adiciona os arquivos ao commit, ignorando arquivos grandes
git add .

# Solicita a mensagem do commit
echo "Digite a mensagem do commit:"
read COMMIT_MSG

# Cria o commit
git commit -m "$COMMIT_MSG"

# Verifica se o repositório remoto está atualizado
git pull --rebase $REPO_URL main

# Faz o push das alterações
git push $REPO_URL main

echo "Repositório atualizado com sucesso."


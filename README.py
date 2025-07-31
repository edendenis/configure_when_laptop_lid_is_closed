#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar para agendar o `suspend` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar para agendar o `suspend` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations to configure/install to schedule `suspend` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `suspend`
# 
# `Suspend` (Suspensão), no contexto de sistemas operacionais como o Linux, é um estado de baixo consumo de energia em que o computador entra para economizar energia quando não está sendo usado ativamente. Quando um sistema entra no modo de suspensão, a maioria dos componentes do hardware é desligada ou reduz significativamente seu consumo de energia, incluindo a tela, discos rígidos e outros periféricos. No entanto, a memória RAM é mantida em um estado de baixo consumo de energia para que o sistema possa ser rapidamente retomado a partir desse estado, permitindo que os usuários continuem a trabalhar de onde pararam. O modo de suspensão é útil para laptops e computadores desktop para economizar energia quando não estão em uso, prolongando a vida útil da bateria em laptops e reduzindo o consumo de energia em computadores de mesa, sem a necessidade de desligar completamente o sistema. O usuário pode ativar ou desativar a suspensão manualmente ou configurar o sistema para entrar automaticamente nesse estado após um período de inatividade.

# ## 1. Como configurar/instalar para atualizar agendar o `suspend`no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar para `suspend` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. O comando `systemctl` pode ser usado para isso, mas de uma maneira um pouco diferente. O comando para suspender o sistema imediatamente é: `sudo systemctl suspend`
# 
#     No entanto, para agendar a suspensão, você precisa usar um utilitário como o `at` ou um script com um comando `sleep`, pois o `systemctl` por si só não tem uma função de agendamento embutida.
# 
# 4. **Usando o comando `at:`** Primeiro, certifique-se de que o serviço atd está instalado e em execução:
# 
#     ```
#     sudo apt-get install at
#     sudo systemctl enable --now atd
#     ```
# 
# 5. Depois, use o `at` para agendar a suspensão. Por exemplo, para suspender o sistema em 60 minutos: `echo "systemctl suspend" | sudo at now + 60 minutes`
# 
# 6. Usando um script com `sleep`: Outra abordagem é criar um pequeno script que espera um determinado período de tempo (usando o comando `sleep`) e depois executa o `systemctl suspend`. Por exemplo: `sudo bash -c "sleep 60m; systemctl suspend"`
# 
#     Este comando colocará o sistema em suspensão após 60 minutos.
# 
# Ambas as abordagens são eficazes para agendar a suspensão do sistema. A escolha entre elas depende das suas preferências e necessidades específicas.

# ### 1.1 Código completo para configurar/instalar
# 
# Para configurar/instalar para limpar o histórico dos navegadores no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Agendar suspender no linux:*** https://chat.openai.com/c/bd95f5e5-005d-409a-abb8-3ff9f332a01f (texto adaptado). ChatGPT. Acessado em: 28/01/2024 23:03.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 28/01/2024 23:03.
# 

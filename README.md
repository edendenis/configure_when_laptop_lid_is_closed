# Como instalar o `configure_when_laptop_lid_is_closed` no `Linux Ubuntu`

## Resumo

Neste documento estao descritos os passos basicos para instalar e habilitar o programa `configure_when_laptop_lid_is_closed` no `Linux Ubuntu`.

## _Abstract_

_This document describes the basic steps to install and enable the program `configure_when_laptop_lid_is_closed` on `Linux Ubuntu`._
## Descricao

`configure_when_laptop_lid_is_closed` e um pequeno script que altera o comportamento do Ubuntu quando a tampa do laptop eh fechada. Ele permite definir a acao desejada por meio de um servico do `systemd`.
## 1. Como instalar o `configure_when_laptop_lid_is_closed`

Para instalar o `configure_when_laptop_lid_is_closed` no `Linux Ubuntu`, execute os passos abaixo:

1. Abra o terminal com `Ctrl + Alt + T`.
2. Clone o repositorio e acesse a pasta:

```bash
git clone https://github.com/edendenis/configure_when_laptop_lid_is_closed.git
cd configure_when_laptop_lid_is_closed
```
3. Copie o script principal para `/usr/local/bin`:

```bash
sudo install -m 755 configure_when_laptop_lid_is_closed.sh /usr/local/bin/
```
4. Instale o servico e habilite-o:

```bash
sudo cp configure_when_laptop_lid_is_closed.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now configure_when_laptop_lid_is_closed.service
```

### 1.1 Codigo completo para instalacao

Execute o bloco abaixo para realizar toda a instalacao de uma so vez:

```bash
git clone https://github.com/edendenis/configure_when_laptop_lid_is_closed.git
cd configure_when_laptop_lid_is_closed
sudo install -m 755 configure_when_laptop_lid_is_closed.sh /usr/local/bin/
sudo cp configure_when_laptop_lid_is_closed.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now configure_when_laptop_lid_is_closed.service
```

## Referencias

[1] OPENAI. ***Como instalar configure_when_laptop_lid_is_closed no Linux Ubuntu:*** https://chatgpt.com/c/688af8ea-d364-8321-a2d3-ab76e79015e1. ChatGPT. Acessado em: 31/07/2025.


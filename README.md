# Gossipbot
## Overview
Gossipbot é um bot escrito em python com o objetivo de automatizar o envio de mensagens num canal do discord, cujo tema seja RPG de texto. Com isso, é possível o ganho de experiência nesses canais de forma simples e rápida.

## Dependencies
* Python 3.8;
* Selenium 1.25.10;
* Chromedriver, compatível com a versão de seu navegador;

## Getting started
1. Faça download do [chromedriver](https://chromedriver.chromium.org/downloads) compatível com a versão mais recente de seu navegador. Feito isso, coloque o arquivo executável dentro da pasta "src";
2. Na pasta settings/, abra o arquivo config.json;
3. Todas as configurações estão estruturadas no formato json. Informe seu usuário, a senha e a URL direta para algum canal do discord que você tenha acesso;
4. Na chave "pauseinterval", especifique o tempo, (em segundos), que o bot deve esperar para enviar a próxima mensagem. Esse intervalo de tempo também é randomizado, sendo ele definido entre o intervalo de tempo definido e o intervalo de tempo x2. Logo, se 300 segundos for especificado, o tempo para o envio de mensagens será randomizado entre 300 e 600 segundos;
5. No arquivo Random Phrases.txt, especifique as frases que você deseja que sejam enviadas no chat. Uma frase por linha. Como o objetivo principal desse bot é automatizar o envio de mensagens num canal de RPG de texto para que se ganhe experiência de forma simples, já há algumas frases previamente especificadas no arquivo;

# ipcheck
Applet to display our external IP address

## Confessional
I got this code by asking [Perplexity](https://www.perplexity.ai/) and then determined that it was OK to commit to my own repo. 

## How it works
The code simply opens a connection to [https://ident.me](https://ident.me), which returns our IP address.

It is the equivalent of doing:
```bash
curl https://ident.me
```

## Proviso
This may not give accurate results when running in a VM
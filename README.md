# easy-password

this project is a good way to manage your password

## Requirements


```bash
sudo apt-get update          
sudo apt-get install xclip
```

## Usage

```bash
python3 password.py --key name-of-your-password | xclip -sel clip
```

## Recommend

```bash
cd /bin
mkdir password
mv project-directory/* /bin/password/
```
next add these aliases:
```bash
alias psw="python3 /bin/password/password.py --key"
alias copy="xclip -sel clip"
```

## New Usage
```bash
psw name-of-your-password | copy
```

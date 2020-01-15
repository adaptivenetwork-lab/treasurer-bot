# treasurer-bot
Bot untuk memanage pemasukan kas laboratory Adaptive Network.

### Development
- Export Variable
```
export TELEGRAM_TOKEN=
export GDRIVE_SHEET_NAME=
```
- Add Google Credentials (credentials.json) in top directory
```
mkdir credentials
```
- Build
```
make build
```
- Run
```
make local-run -e TELEGRAM_TOKEN= -e GDRIVE_SHEET_NAME=
```
- Stop
```
make local-stop
```


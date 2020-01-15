ORG := adaptivenetwork-id
APPS := treasurerbot
DIR := $(CURDIR)


build:
			docker build -t $(ORG)/$(APPS):latest .

local-run:
			docker run --name $(APPS) -e TELEGRAM_TOKEN=$${TELEGRAM_TOKEN} -e GDRIVE_SHEET_NAME=$${GDRIVE_SHEET_NAME} -v '$(CURDIR)/credentials/':'/app/credentials/' -t $(ORG)/$(APPS):latest

local-stop:
			docker stop $(APPS)
			docker rm $(APPS)

		


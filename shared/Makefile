build:
	mkdir -p ./dist
	cp ./src/main.py ./dist
	cd ./src && zip -r ../dist/jobs.zip . -x main.py
	cd ..
	# Use only when libs installed using install command
	cd ./libs && zip -r ../dist/libs.zip . && cd ..

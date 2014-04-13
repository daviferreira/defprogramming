generate_schema:
	./defprogramming/manage.py schemamigration quotes --auto

migrate:
	./defprogramming/manage.py migrate quotes

run:
	./defprogramming/manage.py runserver

gulp:
	cd assets && gulp

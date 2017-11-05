generate_schema:
	./manage.py schemamigration quotes --auto

migrate:
	./manage.py migrate quotes

run:
	./manage.py runserver

gulp:
	cd assets && gulp

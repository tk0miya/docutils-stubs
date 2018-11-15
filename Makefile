.PHONY: release

release:
	python setup.py clean egg_info bdist_wheel sdist
	twine upload dist/docutils*

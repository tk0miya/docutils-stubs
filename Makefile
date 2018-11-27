.PHONY: release
release:
	python setup.py clean egg_info bdist_wheel sdist
	twine upload dist/docutils*

.PHONY: check
check:
	find docutils-stubs -name '*.pyi' -print0 | xargs -0 flake8
	test -e docutils || ln -sF docutils-stubs/ docutils
	mypy docutils

MD_SOURCES=$(wildcard notebooks/*.md)
PY_SOURCES=$(wildcard notebooks/*.py)
NOTEBOOKS=$(patsubst notebooks/%, jupyter/%, $(MD_SOURCES:.md=.ipynb)) $(patsubst notebooks/%, jupyter/%, $(PY_SOURCES:.py=.ipynb))
MEDIA_SRC=$(wildcard notebooks/media/*)
MEDIA_DEST=$(patsubst notebooks/media/%, jupyter/media/%, $(MEDIA_SRC))
DATA_SRC=$(wildcard notebooks/data/*)
DATA_DEST=$(patsubst notebooks/data/%, jupyter/data/%, $(DATA_SRC))
STATIC_SRC=$(wildcard notebooks/_static/*)
STATIC_DEST=$(patsubst notebooks/_static/%, jupyter/_static/%, $(STATIC_SRC))

update: update_medias update_data update_static $(NOTEBOOKS)
	@echo "All good 🥳"

update_medias: $(MEDIA_DEST)
	@echo "Medias OK 👍"

update_data: $(DATA_DEST)
	@echo "Data OK 👍"

update_static: $(STATIC_DEST)
	@echo "Other static assets OK 👍"

clean: 
	@echo "🧹 Removing Jupyter notebooks..."
	@rm -rf jupyter

re: clean update

jupyter:
	@echo "📁 Creating jupyter/..."
	@mkdir jupyter

jupyter/%.ipynb: notebooks/%.md jupyter
	@echo "👉 Converting $< to $@...  "
	@jupytext --from md:myst --to ipynb "$<" -o "$@" >>/dev/null

jupyter/%.ipynb: notebooks/%.py jupyter
	@echo "👉 Converting $< to $@...  "
	@jupytext --from py:percent --to ipynb "$<" -o "$@" >>/dev/null

jupyter/media:
	@echo "📁 Creating jupyter/media/..."
	@mkdir -p jupyter/media

jupyter/media/%: notebooks/media/% jupyter/media
	@echo "🚚 Updating $(basename $<) in jupyter/media"
	@cp "$<" "$@"

jupyter/data:
	@echo "📁 Creating jupyter/data/..."
	@mkdir -p jupyter/data

jupyter/data/%: notebooks/data/% jupyter/data
	@echo "🚚 Updating image $(basename $<) in jupyter/data"
	@cp "$<" "$@"

jupyter/_static:
	@echo "📁 Creating jupyter/_static/..."
	@mkdir -p jupyter/_static

jupyter/_static/%: notebooks/_static/% jupyter/_static
	@echo "🚚 Updating $(basename $<) in jupyter/_static"
	@cp "$<" "$@"

.PHONY: default re clean update update_medias update_data update_static

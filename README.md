# rebuild-papers
Repo to manually re-build papers/ideas to get foundational knowledge of different tools/methodologies

Under src/ there are multiple directories:
    - rebuild_papers/ is my attempt to build out papers to understand them better
    - other_concepts/ is me using established concepts to understand them better

This is it for now. It makes understanding things easier if you build them, and if you can't rebuild them may as well try to use them.

Conda env commands:
    conda env create -f environments/conda.yml
    conda env remove -n condaenv

Create lock file:
    - conda activate condaenv (must run command below while condaenv is activated)
    - conda env export --no-builds > environments/condaenv.lock.yml


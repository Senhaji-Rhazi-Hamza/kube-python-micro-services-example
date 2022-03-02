
# If the first argument is "run"...
ifeq (run,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  
  # ...and turn them into do-nothing targets
  # REF : https://stackoverflow.com/questions/2214575/passing-arguments-to-make-run
  $(eval $(RUN_ARGS):;@:)
endif

cli:
	sh bin/cli.sh $(RUN_ARGS)

.PHONY: run
run : cli
	@echo RUNED CLI

TOTO TATA:;
	@echo $@



# action:
# 	@echo action $(filter-out $@,$(MAKECMDGOALS))



# # clitest:
# # 	sh bin/test.sh

# test:
# 	@echo $(call args,defaultstring)

# action:
# 	echo action $(filter-out $@,$(MAKECMDGOALS))
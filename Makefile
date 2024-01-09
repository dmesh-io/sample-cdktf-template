@PHONY: synth
synth:
	@cdktf synth

@PHONY: apply
apply:
	@cdktf apply

@PHONY: destroy
destroy
	@cdktf destroy

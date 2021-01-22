"""
Machine Learning Model 
"""
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer


class TextGenModel():
    
    def __init__(self, inp_context):
        # user input context
        self.inp_context = inp_context
        # the transformers
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        # add the EOS token as PAD token to avoid warnings
        self.model = TFGPT2LMHeadModel.from_pretrained("gpt2",
                pad_token_id=self.tokenizer.eos_token_id)

    def textGenBeamModel(self):

        model_type = "beam_ngram_penality"

        # encode context the generation is conditioned on
        input_ids = self.tokenizer.encode(self.inp_context, return_tensors='tf')
        print(f"Input Ids : {input_ids}")

        # avoid repetitions of the same word sequences 
        # by setting up n-grams penality
        beam_output_ngram_penality = self.model.generate(input_ids,
                        max_length=50, num_beams=5, early_stopping=True,
                        no_repeat_ngram_size=2)
        print(f"beam_output_ngram_penality : {beam_output_ngram_penality}")

        decoded_beam_output_ngram_penality = self.tokenizer.decode(
                            beam_output_ngram_penality[0],
                            skip_special_tokens=True)
        print(f"Decoded resp: {decoded_beam_output_ngram_penality}")

        return (decoded_beam_output_ngram_penality, model_type)    
    

    

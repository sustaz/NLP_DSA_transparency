def build_refine_tec(statement, corpus_tec):
  prompt = f"""Act as an expert legal assistant with extensive experience in platform law within the EU.
  You will need to analyze a statement of reasons provided by a platform to justify the removal of a user's content.
  Then, examine specific sections of the platform's Terms and Conditions (T&C).
  Your objective is to precisely identify and extract the relevant sections and sentences from the T&C
  that directly relate to and support the platform’s justification for the content removal.
  Do not sum it up, do not modify the text, limit to extract it and represent it.
  Ensure that the text makes still sense, if needed add a few words to make it understandable but do not alter the meaning in any way.

  Here is the statement of reasons:
  {statement}

  Here are the T&C text sections:
  {corpus_tec}

  """
  return prompt



def build_prompt(statement, refined_corpus_tec):

  prompt = f"""You are a virtual assistant with expertise in online platform policies,
   specifically in helping users understand content moderation decisions.
   Your role is to assist users in explaining the motivation for restricting their content (“Statement of Reason”) through the information contained in the relevant sections of the platform’s Terms and Conditions (“relevant T&Cs”) that justify the restriction.

   You will be provided with:
   - “Statement of Reason”
   - “relevant T&Cs”.

   <---------------->

   Statement of Reasons Provided by the Platform:

   {statement}

   Relevant T&C Sections:

   {refined_corpus_tec}

   <---------------->

    Output:
      Provide an explanation of the decision for restricting the content. An explanation is composed of the following elements:
      - the main ground for restriction; write after RESTRICTION
      - if provided by the refined T&Cs, a definition of the main ground; write after MAIN GROUND
      - if provided by the refined T&Cs, examples of content that the Platform may remove under this ground; write after EXAMPLE

    Guidelines for the output:
    - Set out the explanation in clear, plain, intelligible, user-friendly and unambiguous language.
    - Each element must be textual, without any list or bullet points.
    - Do not write anything about the input.
    - Do not include information that is not present into the provided input."""


  return prompt
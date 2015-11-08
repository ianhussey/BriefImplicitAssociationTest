# Created by
Ian Hussey (ian.hussey@ugent.be)

# Last change
19/10/2015

# Version number
0.8

### NB this code has not been independently checked to make sure that it functions as intended.

# Notes
- To my knowledge, this implementation has good fidelity to Millisecond's Inquisit script. However, all instructions are hard coded, making it slightly more difficult to customize the domain or language.
- The current version does not allow you to alter the order of block presentation within the task (e.g., whether participants get flowers good or insects good first). If you want a version with the alternative block order, you can create a second copy of the task folder and use the alternative stimulus file. Future versions might make this possible with a preparatory loop, but it’s more effort than it’s worth right now.
- The escape key quits the task at any time. E, I, or the return key ends the task properly once it’s complete.
- You can run either the psyexp file or the py file inside PsychoPy. The py file should have greater cross platform support; if you run into errors with the psyexp file use the py instead.
- psydat and csv files are produced for each participant. csv file alone is sufficient to most analyses (e.g., calculation of D scores).
- Block length is a function of the number of rows in the stimuli.xlsx file. In order to retain the desired block lengths (e.g., 20 in the first block), 5 exemplars are needed per trial-type. If you wish to use more exemplars per trial-type this will need code changes; probably an overhaul of how each stimulus pool is sampled.
- ITI is set to 250 ms (see Nosek et al., 2007: the IAT at age 7).

# Block layout
The current version follows the block layout described in Nosek et al. (2015: the Brief Implicit Association Test).

4 exemplars per stimulus class. Changing this would require us to add trial counters and “loop.finished = true” code snippets in order to preserve block lengths.

- Block 1 (categories) 4 Trials (1 loop of 4)
- Block 2 (categories + attributes) 16 Trials (1 loop of 16)
- Block 3 (reversed categories) 4 Trials (1 loop of 4)
- Block 4 (reversed categories + attributes) 16 Trials (1 loop of 16)
  - (x2 loops of the above four blocks)

# Known issues
1. If participants get 100% of trials correct on either blocks 3&4 or 6&7 then one of two incorrect response RT columns will not be created for that participant. However, this is not a problem if you merge files across participants based on column header matching (e.g., using plyr’s `rbind()` command). However, it can be problematic if your data processing workflow relies on column ORDER rather than column header NAME, e.g., a SPSS script using a GET command.

2. Instruction screens are hard coded rather than pulled from the excel files, making changing the domain or translating the task slightly more work. Future changes could change this.

3. As of 1.80, the PsychoPy builder allows you specify which range of rows should be included in a given loop. A future change could therefore reorganize the stimulus file so that the first four rows are used in the categories blocks, and all rows are used in the categories + attributes blocks. This would reduce the stimuli files from two to one, making them easier to change.

4. The four trials in the pre block are not sampled randomly from the larger pool of exemplars, as in the inquisit version. This is not a huge problem as the Nosek et al. (2014) paper specifies that these four trials are not used in the calculation of D scores, but it could be corrected with some effort. E.g., a trial counter and a conditional "loop.finished = True".

5. For clarity, references to "target" stimuli could be changed to "category" stimuli throughout to match the nomenclature used in the literature.

6. Component naming is non-intuitive throughout. Could do with a tidy up to allow increase the readability of the .py file.

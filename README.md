# 2024-eahuactz-thesis
Thesis data repository for Emilio Ahuacztin-Garcia

finalthesisfixedfigureEmilio.pdf contains the final text of the thesis.

Figures.zip is a zipped folder containing all of the figures and images used in the thesis

This repository is broken into four folders

FISPACT holds the inventoryW.i script used to run the FISPACT-II simulations. It is altered for each composition, and used in place of the inventory.i file in the FNS_Inconel example provided in FISPACT-II and detailed in the manual

SRIM holds the SRIM output files used to determine dpa and damage depths for each of the material compositions

TGSData holds the calibration, raw TGS data, and traces for each composition

processing holds the files used to process the tgs data, other than the scripts linked to elsewhere. FISPACTresuls.xlsx holds the results from the FISPACT simulations and associated graphs. ResultsSheet.xlsx contains the diffusivity vs dpa with error for each composition. The "Vacancies to DPA Sheet...xlsx" series holds the end results of the TGS processing scripts, and takes in the SRIM data to produce dpa vs thermal diffusivity data. bars.py produces the bar chart comparing diffusivity before and after irradiation. damagedepth.xlsx is used to produce the visualization of the implanted ions and dpa vs depth image, along with the damageviscode.py script. The visualizer.py script produces the traces comparing dpa vs depth for all compositions.

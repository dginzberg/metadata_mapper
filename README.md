
# Metadata Mapper 

[Diagram](https://acacg-my.sharepoint.com/:u:/g/personal/daniel_ginzberg_acaglobal_com/ESYq4X_7jVVGjkrTiS7fY5cBNAiClqaaSkHM3MQRAr_kbA ) 
(still needs some detail but the application layout is present)

  __DEV:__
- REPO is set up with vscode settings preset for easy sharing
            - check rec extensions for vscode workspace
 __Environments:__
    (prepped two to make sure it would work within two application instances)

- UAT: ecomms-scripts\UAT\onBox\catelas\shared\scripts\metadata_mapper\.uatvenv
            - current issue: env activates for PROD automatically but not for UAT
            - might need to 'deactivate' UAT
        - PROD: ecomms-scripts\PROD\onBox\catelas\shared\scripts\metadata_mapper\.prodvenv

__Prior to running:__
- metadata_mapper\metadata_mapper\utils_pkg\constants.py
            - update: 
                - ingestion_dir : input files
                - output_dir : final_output
                - speechmatics_dir : speechmatics input dir
                - log_dir : ligging dir
        

 __SETUP AND RUN__
    1. cd ecomms-scripts\[UAT | PROD]\onBox\catelas\shared\scripts\metadata_mapper
    2. source \[.uatvenv | .prodvenv]\Scripts\activate
    3. pip install .
        - finds packages and installs them to venv
        - packages into .egg
    4. metadata_mapper 


  - [ ] logging points
          [ ] automate build
          [ ] env fixes and cleanup 

# ENA converter in ARC2REPO
:computer: We now have a single-page-application [web app](https://nfdi4plants.github.io/arc2repo/), testing and feedback are very welcome :smiley:   
Please use [arcCommander version 0.2.1](https://github.com/nfdi4plants/arcCommander/releases/tag/v0.2.1-linux.x64) to create the JSON to convert  
A  prototype of ARC to ENA converter with docker image  
requirement: python3.10 is required for xml support.
- basic usage: `python3.10 ena-converter.py`  
- arguments:  
  -a \<json file from arc\>  
  -m \<mapping file\>  
  example: `python3 ena-converter.py -a inv.json -m mapping_ERC000037.xlsx`

to test the converter, you can run it in the docker with prepared dockerfile
Following commandlines can be used to build and run the docker image/container
- Build: `docker build --tag arc2repo .`
- Run: `docker run -d --name a2r arc2repo`
- Copy the file to local: `sudo docker cp a2r:/arc2repo .`

You can also modify the input argument of the python script from docker commands, for example:
- Run: `docker run -d --name a2r arc2repo python3 ena-converter.py -a inv.json -m mapping_ERC000037.xlsx`


## Input: inv.json
inv.json is a output of ARCcommander
See explaination here https://github.com/nfdi4plants/arcCommander/pull/66
`arc export` exports full arc as `investigation.json`

## Output: STUDY.XML
STUDY.XML is one of the accepted file of ENA
See explaination here https://www.ebi.ac.uk/ena/browser/submit
To access the generated files, you could use `sudo docker cp a2r:/arc2repo .` to copy them from the docker container.

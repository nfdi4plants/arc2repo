# ENA converter in ARC2REPO
A  prototype of ARC to ENA converter with docker image  
requirement: python3.10 is required for xml support.
- basic usage: `python3.10 ena-converter.py`  
- arguments:  
  -a \<json file from arc\>  
  -m \<mapping file\>  
  example: `python3 ena-converter.py -a inv.json -m mapping_ERC000037.xlsx`

to test the converter, you can run it in the docker with prepared dockerfile
Following commandlines can be used to build and run the docker image/container
- Build: `docker build --tag arc-to-ena .`
- Run: `docker run -d --name a2e arc-to-ena`

You can also modify the input argument of the python script from docker commands, for example:
- Run: `docker run -d --name a2e arc-to-ena python3 ena-converter.py -a inv.json -m mapping_ERC000037.xlsx`


## Input: inv.json
inv.json is a output of ARCcommander
See explaination here https://github.com/nfdi4plants/arcCommander/pull/66
`arc export` exports full arc as `investigation.json`

## Output: STUDY.XML
STUDY.XML is one of the accepted file of ENA
See explaination here https://www.ebi.ac.uk/ena/browser/submit

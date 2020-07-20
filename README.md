# computer_network_visualisation
Using Dash Cytoscape to visualise networks from a packet capture

![Network Layout](https://github.com/ejooco/computer_network_visualisation/blob/master/example.gif)

## Installation
Clone Repo
```
git clone git@github.com:ejooco/computer_network_visualisation.git
```

### Create Virtual Environment
```
virtualenv venv
```
### Activate Virtual Environment

Windows
```
.\venv\Scripts\activate.bat
```
Linux
```
source venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run App
```
python app.py
```

## Insert your own Data
![Real Example](https://github.com/ejooco/computer_network_visualisation/blob/master/real_data.gif)

Export your pcap to a csv

**Open csv_to_json.py**

Change line 3 from:
```
data = pd.read_csv('test_large1.csv')
```
to...
```
data = pd.read_csv('your_file.csv')
```

Run the script
```
python csv_to_json.py
```
The script will parse the csv and convert it to json

It will create links between each IP address and also calculate the weight (how many packets) of each interaction.

The weight functionality is not used by app.py at this stage but will be used in future iterations to adjust the line thickness of each link to add another dimension to the visualisation.


**Open app.py**

At line 8, change:
```
with open('net.json', 'r') as f:
    data = json.load(f)
```
to...
```
with open('yourfile.json', 'r') as f:
    data = json.load(f)
```
### Run App
```
python app.py
```

## Adjust the layout
Nodes can be clicked and dragged to adjust the layout

Alternatively, you can specify a layout to load within **app.py**

Line 15
```
'name': 'random',
```
This shows a random layout which can be good for initial exploratory analysis.

To play with different layouts, change *random* to any of the following:
* grid
* circle
* concentric
* breadthfirst (this is used in the top example image)
* cose

## To Do
* Add some styling
* Add weight to links
* Automate parent nodes within csv_to_json.py





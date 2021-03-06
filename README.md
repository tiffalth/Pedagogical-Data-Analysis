# Pedagogical Data Analysis Project
An analysis of user traffic data collected from eCHIRP, a UBC-hosted server with resources to support students' learning of UBC Chemistry curriculum.
User data (omitted in the repo) is collected as a JSON file, with the analysis done in Python.

## Project Status
This project is primarily completed. 
Further areas of improvements include building a more suitable host to display all the graphs, instead of loading them one by one, and further refining the code.

## Project Screenshots
Analyzing how often students access videos in the server through histogram of student ID to number of views (student ID blurred for confidentiality purposes)

![image](https://user-images.githubusercontent.com/55005753/165621962-f0cf33ef-58e8-4209-8fe3-6209e2d892ae.png)

Analyzing students' interaction with watching interactive videos vs non-interactive videos.
In here, we define interactive videos as videos with clickable elements in it (e.g. A question students can answer embedded in the video)

![image](https://user-images.githubusercontent.com/55005753/165622105-a667bc6c-c28f-4bd3-9a8f-07136a37cbfa.png)

Analyzing progression of actions students take when they watch a video (student ID blurred for confidentiality purposes)

![image](https://user-images.githubusercontent.com/55005753/165622221-f5e29cfb-c554-47ef-8418-26c63a64795a.png)

## Setup
This project is done entirely in Python 3.9.

Additionally, You will also need to download the following packages to work with this repository.
- Pandas~=1.2.3
- Plotly~=5.6.0

## Reflection
This was a 4-month long project built during my co-op position as a Learning Technology Rover at UBC Skylight: Science Centre for Learning & Teaching. Project goals included learning on to code in Python (something I have never done before) and familiarizing myself with analyzing complex data structures.

One of the main challenges while working on this project was obviously learning Python from scratch and how to use it properly to work with large datasets. This lead me to spend several days going over many Python and its libraries (mainly 'Pandas' and 'Plotly') documentations. While I had originally wanted to go further and create a dashboard for visualization of the graphs, this was unfortunately not possible due to project time constraints. 

At the end of the day, the technologies implemented in this project are 'JSON', 'Pandas' and 'Plotly', all using Python. I chose to use the following libraries in their easier transition to transform large blocks of datas into more accessible dataframes and its visualization potential. In the future, I hope to explore using 'Dash' to further work upon data visualization.

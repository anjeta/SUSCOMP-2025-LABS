# Personal CO2 Footprint Estimation

The goal of today is to explore your own use and energy data demand of the digital infrastructures and appliances you use, and put this into contrast with other household appliances. The focus is on direct energy and how this links to usage patterns.

## Startup Task

Start by setting up git as [per these instructions](https://github.com/anjeta/SUSCOMP-2025-LABS/tree/main/github-repo-setup).

Spend a few minutes writing a list of the digital and electronic technology you use most in the home. You should aim for 3-5 technology-enabled appliances (i.e., with a digital processor and/or Internet or WiFi connected). This could include smart TVs, computers, games consoles, Wifi routers, smart speakers, etc.

1. Take a photo of it to remind yourself of your inventory
2. If possible/safe to do so, take a picture of the label which explains its energy use requirement in Watts (this might be listed on a power adapter in some cases)
3. Write down the item, make notes of any attached speaker systems, external hard drives, or other items that are needed to enable it to work (e.g., a PC will normally have an external monitor, maybe speakers, and so on)

You will need this to help you with the in-lab task this week.

## Task

Time available: 1 hour.

- Get started with markdown, see [how to use markdown](https://www.markdownguide.org/) - 10 minutes
- Make sure you have an up-to-date copy of your coursework repo available (```git clone``` or ```git pull``` as needed to ensure you are up to date with the server). In the ‘week2-personal-co2-footprint’ folder, create a new markdown document called ```username-week2-labnotes.md``` with your markdown editor of choice. Replace ```username``` with your login ID (mine would be ```anjeta```). Create it inside your ```week2-personal-co2-footprint``` repository folder, i.e., the same folder as this file.

1. For each photo, and while you have time in the lab, put a subheading that describes it.
2. Add a little detail on how often you use it and for how long (estimate hours per day, week, and year)
3. Using your photos and the resources below, look up how much active power the device uses when in use, and add this to a markdown table under the appropriate heading.
4. If the device has a different power level when not in use (e.g., on standby or 0 W if powered off when not in use), find out what this is and add it to the table.
5. Finally, add a row that calculates the number of kilowatt/hours (divide total in Watts by 1,000 and multiply by the number of hours of use) based on your estimate of use per day, week, and year. For example, if you had a smart speaker that takes 5 W all year round, this would be: 5 × 365 × 241000 = 43.8 kWh

   - i.e., 365 days in a year by 24 hours per day to get total hours used, multiplied by the power demand in Watts to get Watt-hours
   - divide by 1000 to get kilowatt hours

6. The task should be time-bound, i.e., you should not spend much more than 40 minutes of concentrated time on this task. I would expect you to find and calculate the power for 3-5 assets in detail within this time.
7. Add a subsection ```## Reflections``` with a short paragraph on your thoughts on how the various assets compare with one another. Which uses the most energy, which uses the least, and how does this relate to the use time or overall powered-on time

Don’t forget to ```git add``` your new file, ```commit```, and ```push``` to the server at least at the end of the task.

## Extension task

Time available: 30 minutes.

Try to approximate:

- The amount of energy used by network traffic arising from your use of the Internet
- Add a further paragraph to your reflections discussing how this compares to the direct energy use of your device
- How does this compare to a typical washing machine, refrigerator, or domestic oven with the use pattern found in your household?

We will not worry about the cloud computing data centres, AI workloads, or other energy demands that might be triggered by your device use for now.

## Learning outcomes

- You should have an appreciation of the direct energy requirements of the devices you use most often.
- You should appreciate their relative energy requirements and how this relates to use.
- How the impact of time affects the cumulative energy requirement (i.e., amount over a year).
- You should be increasing your energy literacy.

## Starting points

Here are some useful digital resources to help.

- [Typical home appliance energy demand summary sheet](https://www.nea.org.uk/wp-content/uploads/2022/03/Electricity-Consumption-Around-the-Home.pdf)
- [Household energy and transportation fuel consumption in Slovenia](https://kazalci.arso.gov.si/en/content/household-energy-and-transportation-fuel-consumption-2?utm_source=chatgpt.com)
- Climate Savers Computing Initiative on [Wikipedia](https://en.wikipedia.org/wiki/Climate_Savers_Computing_Initiative)
- [What appliances use the most electricity](https://energysavingtrust.org.uk/top-five-energy-consuming-home-appliances/)?
- Energy ratings on [energysavings trust](https://energysavingtrust.org.uk/advice/home-appliances/)
- What is a kilowatt/hour (kWh)? ([YouTube](https://www.youtube.com/watch?v=SMPhh8gT_1E))
- Calculating your personal footprint using the [Consumer Footprint Calculator](https://eplca.jrc.ec.europa.eu/ConsumerFootprint.html?utm_source=chatgpt.com)

## Acknowledgement

This lab excercise is made based on the materials from the Sustainable Computing course held by Adrian Friday, a Professor of Computing and Sustainability at Lancaster University.

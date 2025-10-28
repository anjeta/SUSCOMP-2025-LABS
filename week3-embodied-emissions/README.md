# Estimating Embodied Emissions

The goal of today is to explore the ‘carbon footprint’ (related to embodied energy) of your own digital appliances and devices that you identified last week. Unlike direct energy use, the energy here is required at all stages of the manufacturing pipeline, so the carbon footprint relates to mining of raw materials, processing, transportation, manufacturing, and all the other items that come together to make your products and get them in your hands.

## Cautionary Note

The carbon footprint of each device is at best an estimate of the average or typical embodied energy, as the supply chains are very long and complex. They also differ between even similar products, and change over time (e.g., a market might source from different suppliers).

1. You may get differences in estimates, or only be able to get an estimate for a device that’s as similar as possible.
2. Sometimes manufacturers and resellers will list the carbon footprint. There are always questions we should ask about whether we can rely on the data - data can be old, contain errors, or it may be in their interest to ‘scope’ the estimate to make their products look good.
3. We may have to start caring more about data quality, e.g., published peer reviews in reputable journals with ‘life cycle assessments’ (LCA) analysis are likely to be the most reliable sources.

Since this is just a short lab task, approximate ‘ball park’ estimates are good enough to ‘get an idea’.

## Task

Time available: 1 hour.

Make sure you have an up to date copy of your coursework repo available (```git clone``` or ```git pull``` as needed to ensure you are up to date with the server), as before. In the ‘week3-embodied-emissions’ folder, create a new markdown document called ```username-week3-labnotes.md```, where ‘username’ is, of course, your username.

1. For each photo that you used last week, put a subheading that describes it.
2. Look up the carbon footprint of the device’s manufacture.
3. Add a table. Bring over the annual energy use of the device based on your use pattern. Add a column converting this to CO2e by multiplying by a conversion factor (take care with your units!). In Slovenia, you can assume the energy mix is [0.235 kg CO2e/kWh](https://ceu.ijs.si/izpusti-co2-tgp-na-enoto-elektricne-energije/)
4. Add a column with the carbon footprint for the device.
5. Now add a row comparing the use footprint with the embodied footprint. Multiply the use footprint by the number of years you keep the device to get the total direct energy for that many years of use; calculate the ‘footprint per year’ of the  manufacturing footprint.
6. You should add a row for 1, 3, 5, and 10 years. In reality, some devices have shorter lifespans than this, but many (e.g., TVs, ovens) could last much longer.
7. Add a subsection ## Reflections with a short paragraph on your thoughts on how the various assets compare with one another, especially reflecting on the use phase related energy against the manufacturing or embodied energy.

**In your report, specify which data sources you used and provide reasons for choosing them.**
Don’t forget to git add your new file, commit, and push to the server at least at the end of the task.

## Learning outcomes

- You should have an appreciation of how the embodied energy varies with the appliances and devices you use most often
- You should appreciate how embodied energy is amortised over the life of the device, and how this varies with longevity
- You should see how the use phase and the embodied phase vary considerably across devices
- You should be gaining some or enhancing your ‘carbon literacy’.


## Starting points

Here are some useful digital resources to help. In your report, specify which ones (or others) you actually use. Don’t forget, these are starting points, and their quality is not guaranteed! You should always have an open and enquiring mind when it comes to data sources.

- [Living Sustainability: In-Context Interactive Environmental Impact Communication](https://github.com/iamZhihanZhang/Living-Sustainability)
- [CO2 Everything](https://www.co2everything.com/) - volunteer effort, so make sure to check the data!
- [Cloud carbon footprint calculator](https://www.cloudcarbonfootprint.org/)
- [Internet use footprint](https://ecotree.green/en/calculate-digital-co2)
- [Mobile data traffic outlook](https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/mobile-traffic-forecast)
- [University of Oxford IT provided figures](https://www.it.ox.ac.uk/article/environment-and-it) - worth reading anyway
- For fun, Small World [Personal carbon footprint calculator](https://www.sw-consulting.co.uk/carbon-calculator)
- [Ethical consumer guides, including technology](https://www.ethicalconsumer.org/)

## Acknowledgement

This lab exercise is made based on the materials from the Sustainable Computing course held by Adrian Friday, a Professor of Computing and Sustainability at Lancaster University.

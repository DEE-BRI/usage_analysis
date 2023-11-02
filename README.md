# Usage Analysis

Usage Analysis refers to a method of estimating electricity, gas, and kerosene consumption by household use based on consumption by energy type, i.e., electricity consumption, gas consumption, and kerosene consumption in the home.
The uses are categorized into heating, cooling, ventilation, hot water supply, lighting, home appliances, and cooking. Electricity and gas consumption and kerosene consumption should be available on a monthly basis from receipts and other sources.

## Input items

- Number of persons in the household
- Floor area of main living room
- Floor area of other living rooms
- Total floor area
- Check energy source and monthly energy consumption and whether used for heating/cooling
- Adjustment factor for each type of equipment

Please check sample/input.csv for specific information.

## Output items

- Energy consumption by energy source, month, and facility type

Please refer to sample/output.csv for details.

## Input/output format

Assume CSV file. Perform a calculation for each line of the input CSV file and output the same number of lines in the output file.

## Command line example

```
python3 src/bunkai.py -i input.csv -o out.csv
```
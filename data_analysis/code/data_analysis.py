import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

Countries = ['argentina.csv', 'australia.csv', 'brazil.csv', 'canada.csv', 'china.csv', 'france.csv', 'germany.csv', 'india.csv', 'indonesia.csv', 'italy.csv', 'japan.csv', 'mexico.csv', 'russia.csv', 'saudi_arabia.csv', 'south_africa.csv', 'south_korea.csv', 'turkey.csv', 'united_kingdom.csv', 'united_states.csv']
for i in Countries:
    df = pd.read_csv(i)
    df.head()

    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x='Year', y='GDP(US $)', label='GDP')
    plt.title('Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP(US $)')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x='Year', y='Energy Consumption(TJ)', label='Energy Consumption')
    plt.title('Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Energy Consumption(TJ)')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x='Year', y='CO2 Emission(kt)', label='CO2 Emissions')
    plt.title('Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emission(kt)')
    plt.legend()
    plt.show()

    corr_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

    ! pip install plotly

    fig = px.scatter_3d(df,
                        x='GDP(US $)',
                        y='Energy Consumption(TJ)',
                        z='CO2 Emission(kt)',
                        color='CO2 Emission(kt)',  # Optional: color by CO2 Emissions
                        title='3D Scatter Plot of GDP, Energy Consumption, and CO2 Emissions')

    # Show the plot
    fig.show()


```python
import pandas as pd
```


```python
df = pd.read_csv('donic.tsv', sep='\t')
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Speed</th>
      <th>Spin</th>
      <th>Tackiness</th>
      <th>Overall</th>
      <th>Price</th>
      <th>Ratings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Donic Baracuda</td>
      <td>8.7</td>
      <td>9.5</td>
      <td>2.3</td>
      <td>9.3</td>
      <td>40</td>
      <td>198</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Donic Acuda S2</td>
      <td>8.8</td>
      <td>9.1</td>
      <td>2.6</td>
      <td>9.2</td>
      <td>37</td>
      <td>108</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Donic Bluefire M1</td>
      <td>9.3</td>
      <td>9.3</td>
      <td>2.7</td>
      <td>9.3</td>
      <td>54</td>
      <td>81</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Donic Acuda S3</td>
      <td>8.4</td>
      <td>9.1</td>
      <td>1.8</td>
      <td>9.0</td>
      <td>52</td>
      <td>73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Donic Acuda S1</td>
      <td>9.2</td>
      <td>9.2</td>
      <td>1.9</td>
      <td>9.2</td>
      <td>52</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Speed</th>
      <th>Spin</th>
      <th>Tackiness</th>
      <th>Overall</th>
      <th>Price</th>
      <th>Ratings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>79</th>
      <td>Donic Solo</td>
      <td>7.0</td>
      <td>7.5</td>
      <td>2.0</td>
      <td>7.9</td>
      <td>12</td>
      <td>1</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Donic Traction II</td>
      <td>8.5</td>
      <td>9.3</td>
      <td>5.0</td>
      <td>9.2</td>
      <td>54</td>
      <td>1</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Donic Vario Mach 1</td>
      <td>9.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>36</td>
      <td>1</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Donic Vario Sound</td>
      <td>9.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>59</td>
      <td>1</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Donic Vario ST (Tuned)</td>
      <td>7.9</td>
      <td>8.8</td>
      <td>0.0</td>
      <td>7.6</td>
      <td>38</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

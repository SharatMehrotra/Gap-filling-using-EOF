# Gap-filling-using-EOF

<h3>Dataset description</h3>

The InSAR data set used for our study is from the region of Campi Flergi, Italy. The data spans from 2016-09-09 to 2018-05-8 and collected from 13 different geographical points.
The GPS data is divided into 3 subsets- East, North-east, and North and they all span from 2009-01-01 to 2020-09-30. All the 3 subsets were collected from 99 different stations in New Zealand. 


<h3>Introduction</h3>
Missing data in SAR and GPS data sets is an old problem. In SAR images, the reason could be interference suppression technical limitations or just raw data quality.
Missing data causes issues like anomalous system behaviour, long computation time, no stability etc. There is a need for an iterative algorithm which we can use to reconstruct and refine the data.<br>
EOF analysis, has been suggested to retrieve the missing values in data sets. Using the data, we first construct a spatial-temporal matrix. The missing values are then initialized appropriately. The method then decomposes the constructed matrix into different EOF modes. The optimum number of EOF modes are selected such that we are able to cover maximum variability in the data. The matrix is reconstructed using the number of modes calculated. An iterative update of missing values is performed, which gives the best estimate of missing data points. To verify the correctness of this method, 1-2% of the given data has been used as the cross-validation-set, to see if the missing values can be estimated correctly or not.


<h3>Conclusion</h3>
EOF analysis is an iterative algorithm used to predict the missing values in InSAR and GPS data. We can reconstruct and refine the time series without needing any information about the data beforehand. [1] The algorithm initializes the missing values, selects the number of components preserving maximum variability and refines the final matrix till point of convergence. Therefore, the conclusion can be drawn that EOF based gap filling analysis is an effective way of filling missing values in InSAR and GPS data.


The jupiter notebooks are named according to the data set it is using. The beta/ (convergence threshold) can be adjusted as per the refinement needed. 

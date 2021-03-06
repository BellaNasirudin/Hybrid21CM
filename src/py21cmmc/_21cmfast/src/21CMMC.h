/*
    This is the header file for the wrappable version of 21cmFAST, or 21cmMC.
    It contains function signatures, struct definitions and globals to which the Python wrapper code
    requires access.
*/


/*
    --------------------------------------------------------------------------------------------------------------------
    PARAMETER STRUCTURES (these should be trimmed accordingly)
    --------------------------------------------------------------------------------------------------------------------
*/

typedef struct CosmoParams{
    
    unsigned long long RANDOM_SEED;
    float SIGMA_8;
    float hlittle;
    float OMm;
    float OMl;
    float OMb;
    float POWER_INDEX;
    
};

struct UserParams{
    
    // Parameters taken from INIT_PARAMS.H
    int HII_DIM;
    int DIM;
    float BOX_LEN;
    
};


struct InitialConditions{
    float *hires_density;
};

void ComputeInitialConditions(struct UserParams user_params, struct CosmoParams cosmo_params, struct InitialConditions boxes);
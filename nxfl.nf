#!/usr/bin/env nextflow

//params.input = '/home/user/QCEIMS/many_Exp/2-Chloroethanol_GFN2/*'

// Workflow Boiler Plate
// rdkit

//params.dir= '/home/user/QCEIMS/many_Exp/2-Chloroethanol_GFN2/*'
//directories = Channel.fromPath(params.input)
directories = Channel.fromPath('/home/user/QCEIMS/rdk_Exp/*', type: 'dir')
//directories.view()

ch = Channel.of( 1, 3, 5, 7 )
ch.view { "value: $it" }

TOOL_FOLDER = "$baseDir/bin"

process qcxms {
    publishDir "./nf_output", mode: 'copy'

    conda "$TOOL_FOLDER/conda_env.yml"

    input:
    path(coord) from directories


    """ 

    echo ${coord}
    cd ${coord}
    obabel m.mol -O m.tmol
    mv m.tmol coord    
    qcxms
    qcxms
    pqcxms
    getres
    plotms
    """
}
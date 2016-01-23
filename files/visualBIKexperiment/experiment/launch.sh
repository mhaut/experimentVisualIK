# first, open ice storm
#cd ~/robocomp && rcnode &
# second open rcremoteserver
#cd ~ && rcremoteserver &
# launch script
#rcis /home/robocomp/robocomp/components/robocomp-ursus/etc/ursus.xml &
python runExperiment.py --Ice.Config=/home/robocomp/robocomp/components/experimentVisualIK/etc/configDefSim/experiment.conf

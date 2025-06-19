#!/bin/bash

# Archivos de entrada
R1="WH_R1.fastq"
R2="WH_R2.fastq"

# Archivo resumen
SUMMARY="summary_fastqc_results.csv"
echo "ID,Total Sequences,R1_Q30_Percent,R2_Q30_Percent,R1_path,R2_path" > "$SUMMARY"


# Iteraciones
for HEADCR in 3 ; do
	for LEAD in 10 15; do
	  for TRAIL in 10 15; do
   	  	for SW in 15 20; do
    		for MINL in 31 36; do

       			 ID="L${LEAD}_T${TRAIL}_SW${SW}_M${MINL}"
      			 OUTDIR="results/${ID}"
      			 mkdir -p "$OUTDIR/trimmed" "$OUTDIR/fastqc"
			
       			 OUT_R1="${OUTDIR}/trimmed/R1_clean.fastq"
       			 OUT_R2="${OUTDIR}/trimmed/R2_clean.fastq"
       			 UNP_R1="${OUTDIR}/trimmed/R1_unp.fastq"
    		     UNP_R2="${OUTDIR}/trimmed/R2_unp.fastq"

        	     echo "🔧 Trimming: $ID"
      			 TrimmomaticPE -phred33 "$R1" "$R2" \
                  "$OUT_R1" "$UNP_R1" "$OUT_R2" "$UNP_R2" \
                   HEADCROP:$HEADCR LEADING:$LEAD TRAILING:$TRAIL SLIDINGWINDOW:4:$SW MINLEN:$MINL 

                 echo "🔍 Running FastQC..."
                 fastqc "$OUT_R1" "$OUT_R2" -o "$OUTDIR/fastqc"

        		 # Extraer resumen de FastQC
       			 unzip -o "$OUTDIR/fastqc/$(basename "$OUT_R1")_fastqc.zip" -d "$OUTDIR/fastqc" >/dev/null
       			 unzip -o "$OUTDIR/fastqc/$(basename "$OUT_R2")_fastqc.zip" -d "$OUTDIR/fastqc" >/dev/null

       			 R1_DATA="$OUTDIR/fastqc/$(basename "$OUT_R1")_fastqc/fastqc_data.txt"
       			 R2_DATA="$OUTDIR/fastqc/$(basename "$OUT_R2")_fastqc/fastqc_data.txt"

       			 R1_TOTAL=$(grep "Total Sequences" "$R1_DATA" | cut -f2)
       			 R1_Q30=$(grep -A 1 "Per base sequence quality" "$R1_DATA" | tail -n +2 | awk '{ if ($2 >= 30) sum += 1; total += 1 } END { if (total>0) print int((sum/total)*100); else print 0 }')

       			 R2_TOTAL=$(grep "Total Sequences" "$R2_DATA" | cut -f2)
       			 R2_Q30=$(grep -A 1 "Per base sequence quality" "$R2_DATA" | tail -n +2 | awk '{ if ($2 >= 30) sum += 1; total += 1 } END { if (total>0) print int((sum/total)*100); else print 0 }')
	
       			 echo "$ID,$R1_TOTAL,$R1_Q30,$R2_Q30,$OUT_R1,$OUT_R2" >> "$SUMMARY"

     			 done
    			done
  			done
		done
	done	

echo "✅ Proceso completo. Revisa el archivo: $SUMMARY"






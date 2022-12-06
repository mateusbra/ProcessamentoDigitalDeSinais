/* Implementa��o de um filtro M�dia M�vel 
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
Walter vers�o 1.0 
 */
#include <stdio.h>
//#include <fcntl.h>
//#include <io.h>


#define NSAMPLES       100	// Tamanho da m�dia
#define WSAMPLES       100
int main()
{
   FILE *in_file, *out_file, *out_file_erro;
   int i, n, n_amost;
  
   short entrada,saida;
   short sample[NSAMPLES] = {0x0};
   float w[WSAMPLES];
   float y=0;
   float d=0;
   float e=0;
   float u=0.00000000001;
   //Carregando os coeficientes do filtro m�dia m�vel
   
   float coef[NSAMPLES]={
   				#include "CoefPA.dat"
   };
  
 
   /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("..//ruido_branco.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if((out_file_erro = fopen("..//erro2.txt","w"))==NULL)
  {
      printf("\nErro: N�o foi poss�vel abrir o arquivo de sa�da.\n");
      return 0;
  }
  if ((out_file = fopen("..//saida_y.pcm","wb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

   // zera vetor de amostras
   for (i=0; i<NSAMPLES; i++)
        {
        sample[i]=0;
        }
   for (i=0; i<WSAMPLES; i++)
        {
        w[i]=0;
        }
   // execu��o do filtro
 do {
        
	   //zera sa�da do filtro
        y=0;
		    d=0;
        //l� dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
				sample[0] = entrada;

        //Convolu��o e acumula��o
        for (n=0; n<WSAMPLES; n++)
                {
                y += w[n]*sample[n];
                d += coef[n]*sample[n];
                }
		
                
         e = d - y;
         for(n=0;n<WSAMPLES;n++){
         	w[n] = w[n] + u*e*sample[n];
         }       
			       
                
        //desloca amostra
        for (n=WSAMPLES-1; n>0; n--)
                {
                sample[n]=sample[n-1];
                }
		    saida = (short) y;

        //escreve no arquivo de sa�da
        fwrite(&saida,sizeof(short),1,out_file);
        fprintf(out_file_erro, "%f\n", e);
 } while (n_amost);

 		
    for (i = 0; i < WSAMPLES; i++)
        printf("%f\n",w[i]);
   //fecha os arquivos de entrada de sa�da
   fclose(out_file);
   fclose(in_file);
   fclose(out_file_erro);
   return 0;
}

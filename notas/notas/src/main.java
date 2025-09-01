/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */


import java.util.Scanner;

/**
 *
 * @author ESTUDIANTES
 */
public class main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner lector= new Scanner(System.in);
        
         // nextInt para valores enteros
         // nextDoouble para valores decimales
         // next //Leer string de mas de una sola lineqa
         // nexLine // leer string de mas de una linea
         
         System.out.println("ingrese la nota1: ");
         double nota1 = lector.nextDouble();
         
         System.out.println("ingrese la nota2: ");
         double nota2 = lector.nextDouble();
         
         System.out.println("ingrese la nota3: ");
         double nota3 = lector.nextDouble();
         
         double p1 = nota1*0.30;
         double p2 = nota2*0.30;
         double p3 = nota3*0.40;
         
         double nf = p1+p2+p3;
         
         // system.out.println(" ¿la nota final es: " + nf);
         
         if(nf >=3.0) {
             System.out.println("El estudiante APROBO la materia con una nota de : " + nf);
         }else{ 
             System.out.println("El estudiante APROBO la materia con una nota de : " + nf);
             
         }
         
        
        
    }
    
}

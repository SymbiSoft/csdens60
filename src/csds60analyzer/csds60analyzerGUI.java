package csds60analyzer;

/* Archivo: csds60analyzer.java
   Autor: Jorge Aguirre Andreu
   Descripción: Aplicación para visualizar gráficas estadísticas a partir de un archivo
   xml exportado previamente desde la aplicación csds60

    Copyright (C) 2009  Jorge Aguirre Andreu

    This file is part of CSDs60.
    CSDs60 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CSDs60 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.*/

import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.awt.Color;
import java.io.File;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import java.util.*;
import javax.swing.JFrame;
import net.iharder.dnd.FileDrop;
import org.jdom.*;
import org.jdom.input.*;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.time.Day;
import org.jfree.data.time.TimeSeries;
import org.jfree.data.time.TimeSeriesCollection;


public class csds60analyzerGUI extends javax.swing.JFrame{

    BufferedImage grafica = null;
    String fichero=null;

    public csds60analyzerGUI(){
        initComponents();
    }

    public BufferedImage creaImagen(){
        BufferedImage imagen=null;
        try{
            SAXBuilder builder=new SAXBuilder(false);
            Document doc=null;
            TimeSeriesCollection datos = new TimeSeriesCollection();
            if(fichero!=null){
                doc=builder.build(fichero);
                Element raiz=doc.getRootElement();
                List<Element> dias=raiz.getChildren("dia");
                Iterator<Element> diasIT=dias.iterator();
                TimeSeries desayunoAntes = new TimeSeries("Desayuno antes");
                TimeSeries desayunoDespues = new TimeSeries("Desayuno después");
                TimeSeries almuerzoAntes = new TimeSeries("Almuerzo antes");
                TimeSeries almuerzoDespues = new TimeSeries("Almuerzo después");
                TimeSeries cenaAntes = new TimeSeries("Cena antes");
                TimeSeries cenaDespues = new TimeSeries("Cena después");
                while(diasIT.hasNext()){
                    Element diaActual=diasIT.next();
                    Integer fechaActual=Integer.parseInt(diaActual.getChildText("fecha").substring(0,10));
                    
                    Calendar fad=GregorianCalendar.getInstance();
                    fad.setTimeInMillis(fechaActual.longValue()*1000);

                    int dia=fad.get(Calendar.DAY_OF_MONTH);
                    int mes=fad.get(Calendar.MONTH)+1;
                    int ano=fad.get(Calendar.YEAR);

                    if(diaActual.getChildren().toString().contains("desayunoantes")){
                        int desayunoAntesActual=Integer.parseInt(diaActual.getChildText("desayunoantes"));
                        desayunoAntes.add(new Day(dia,mes,ano),desayunoAntesActual);
                    }
                    if(diaActual.getChildren().toString().contains("desayunodespues")){
                        int desayunoDespuesActual=Integer.parseInt(diaActual.getChildText("desayunodespues"));
                        desayunoDespues.add(new Day(dia,mes,ano),desayunoDespuesActual);
                    }
                    if(diaActual.getChildren().toString().contains("almuerzoantes")){
                        int almuerzoAntesActual=Integer.parseInt(diaActual.getChildText("almuerzoantes"));
                        almuerzoAntes.add(new Day(dia,mes,ano),almuerzoAntesActual);
                    }
                    if(diaActual.getChildren().toString().contains("almuerzodespues")){
                        int almuerzoDespuesActual=Integer.parseInt(diaActual.getChildText("almuerzodespues"));
                        almuerzoDespues.add(new Day(dia,mes,ano),almuerzoDespuesActual);
                    }
                    if(diaActual.getChildren().toString().contains("cenaantes")){
                        int cenaAntesActual=Integer.parseInt(diaActual.getChildText("cenaantes"));
                        cenaAntes.add(new Day(dia,mes,ano),cenaAntesActual);
                    }
                    if(diaActual.getChildren().toString().contains("cenadespues")){
                        int cenaDespuesActual=Integer.parseInt(diaActual.getChildText("cenadespues"));
                        cenaDespues.add(new Day(dia,mes,ano),cenaDespuesActual);
                    }
                }
                datos.addSeries(desayunoAntes);
                datos.addSeries(desayunoDespues);
                datos.addSeries(almuerzoAntes);
                datos.addSeries(almuerzoDespues);
                datos.addSeries(cenaAntes);
                datos.addSeries(cenaDespues);
            }
            JFreeChart graficaJfree = ChartFactory.createTimeSeriesChart(
             "Análisis",
             " ",
             "Glucosa (mg)",
             datos,
             true,
             true,
             false
            );
            XYPlot plot=(XYPlot)graficaJfree.getPlot();
            plot.setBackgroundPaint(Color.getHSBColor(0f,0f,.88f));
            plot.setDomainGridlinePaint(Color.getHSBColor(0f,0f,.35f));
            plot.setDomainTickBandPaint(Color.getHSBColor(0f,0f,.93f));
            plot.setOutlinePaint(Color.getHSBColor(0f,0f,0.35f));
            plot.setRangeGridlinePaint(Color.getHSBColor(0f,0f,0.35f));
            XYLineAndShapeRenderer plot2=(XYLineAndShapeRenderer)plot.getRenderer();
            if(!CBdesayunoantes.getState())plot2.setSeriesLinesVisible(0,false);
            plot2.setSeriesPaint(0,Color.getHSBColor(.3f,1f,.5f));
            //plot2.setSeriesStroke(0,new BasicStroke(2.0f,BasicStroke.CAP_ROUND,BasicStroke.JOIN_ROUND,1.0f));
            if(!CBdesayunodespues.getState())plot2.setSeriesLinesVisible(1,false);
            plot2.setSeriesPaint(1,Color.getHSBColor(.2f,1f,.9f));
            if(!CBalmuerzoantes.getState())plot2.setSeriesLinesVisible(2,false);
            plot2.setSeriesPaint(2,Color.getHSBColor(.0f,1f,.6f));
            if(!CBalmuerzodespues.getState())plot2.setSeriesLinesVisible(3,false);
            plot2.setSeriesPaint(3,Color.getHSBColor(.0f,1f,.9f));
            if(!CBcenaantes.getState())plot2.setSeriesLinesVisible(4,false);
            plot2.setSeriesPaint(4,Color.getHSBColor(.6f,1f,.4f));
            if(!CBcenadespues.getState())plot2.setSeriesLinesVisible(5,false);
            plot2.setSeriesPaint(5,Color.getHSBColor(.6f,1f,1f));
            imagen = graficaJfree.createBufferedImage(800, 600);
        }
        catch(Exception e){
            e.printStackTrace();
        }
        return imagen;
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        popupMenu1 = new java.awt.PopupMenu();
        popupMenu2 = new java.awt.PopupMenu();
        CBdesayunoantes = new java.awt.Checkbox();
        CBdesayunodespues = new java.awt.Checkbox();
        CBdesayuno = new java.awt.Checkbox();
        CBalmuerzo = new java.awt.Checkbox();
        CBalmuerzoantes = new java.awt.Checkbox();
        CBalmuerzodespues = new java.awt.Checkbox();
        CBcena = new java.awt.Checkbox();
        CBcenaantes = new java.awt.Checkbox();
        CBcenadespues = new java.awt.Checkbox();
        label1 = new java.awt.Label();

        popupMenu1.setLabel("popupMenu1");

        popupMenu2.setLabel("popupMenu2");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("CSDs60Analyzer");
        setBackground(new java.awt.Color(255, 255, 255));
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setResizable(false);

        CBdesayunoantes.setBackground(new java.awt.Color(255, 255, 255));
        CBdesayunoantes.setLabel("Glucosa antes");
        CBdesayunoantes.setState(true);
        CBdesayunoantes.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBdesayunoantesItemStateChanged(evt);
            }
        });
        CBdesayunoantes.addPropertyChangeListener(new java.beans.PropertyChangeListener() {
            public void propertyChange(java.beans.PropertyChangeEvent evt) {
                CBdesayunoantesPropertyChange(evt);
            }
        });

        CBdesayunodespues.setBackground(new java.awt.Color(255, 255, 255));
        CBdesayunodespues.setLabel("Glucosa después");
        CBdesayunodespues.setState(true);
        CBdesayunodespues.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBdesayunodespuesItemStateChanged(evt);
            }
        });

        CBdesayuno.setBackground(new java.awt.Color(255, 255, 255));
        CBdesayuno.setLabel("Desayuno");
        CBdesayuno.setState(true);
        CBdesayuno.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBdesayunoItemStateChanged(evt);
            }
        });

        CBalmuerzo.setBackground(new java.awt.Color(255, 255, 255));
        CBalmuerzo.setLabel("Almuerzo");
        CBalmuerzo.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBalmuerzoItemStateChanged(evt);
            }
        });

        CBalmuerzoantes.setBackground(new java.awt.Color(255, 255, 255));
        CBalmuerzoantes.setLabel("Glucosa antes");
        CBalmuerzoantes.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBalmuerzoantesItemStateChanged(evt);
            }
        });

        CBalmuerzodespues.setBackground(new java.awt.Color(255, 255, 255));
        CBalmuerzodespues.setLabel("Glucosa después");
        CBalmuerzodespues.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBalmuerzodespuesItemStateChanged(evt);
            }
        });

        CBcena.setBackground(new java.awt.Color(255, 255, 255));
        CBcena.setLabel("Cena");
        CBcena.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBcenaItemStateChanged(evt);
            }
        });

        CBcenaantes.setBackground(new java.awt.Color(255, 255, 255));
        CBcenaantes.setLabel("Glucosa antes");
        CBcenaantes.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBcenaantesItemStateChanged(evt);
            }
        });

        CBcenadespues.setBackground(new java.awt.Color(255, 255, 255));
        CBcenadespues.setLabel("Glucosa después");
        CBcenadespues.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                CBcenadespuesItemStateChanged(evt);
            }
        });

        label1.setBackground(new java.awt.Color(255, 255, 255));
        label1.setText("CSDs60Analyzer 0.1 http://code.google.com/csdens60");

        org.jdesktop.layout.GroupLayout layout = new org.jdesktop.layout.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
            .add(layout.createSequentialGroup()
                .addContainerGap(680, Short.MAX_VALUE)
                .add(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
                    .add(org.jdesktop.layout.GroupLayout.TRAILING, layout.createSequentialGroup()
                        .add(label1, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap())
                    .add(org.jdesktop.layout.GroupLayout.TRAILING, layout.createSequentialGroup()
                        .add(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
                            .add(CBcena, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                            .add(CBalmuerzo, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                            .add(layout.createSequentialGroup()
                                .add(10, 10, 10)
                                .add(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
                                    .add(CBdesayunodespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                                    .add(CBdesayunoantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)))
                            .add(CBdesayuno, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                            .add(layout.createSequentialGroup()
                                .add(10, 10, 10)
                                .add(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
                                    .add(CBalmuerzodespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                                    .add(CBalmuerzoantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)))
                            .add(layout.createSequentialGroup()
                                .add(10, 10, 10)
                                .add(layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
                                    .add(CBcenadespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                                    .add(CBcenaantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE))))
                        .add(47, 47, 47))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(org.jdesktop.layout.GroupLayout.LEADING)
            .add(layout.createSequentialGroup()
                .add(52, 52, 52)
                .add(CBdesayuno, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBdesayunoantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBdesayunodespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBalmuerzo, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBalmuerzoantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBalmuerzodespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBcena, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBcenaantes, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(org.jdesktop.layout.LayoutStyle.RELATED)
                .add(CBcenadespues, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .add(313, 313, 313)
                .add(label1, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE, org.jdesktop.layout.GroupLayout.DEFAULT_SIZE, org.jdesktop.layout.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void CBdesayunoantesPropertyChange(java.beans.PropertyChangeEvent evt) {//GEN-FIRST:event_CBdesayunoantesPropertyChange

    }//GEN-LAST:event_CBdesayunoantesPropertyChange

    private void CBdesayunoantesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBdesayunoantesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBdesayunoantesItemStateChanged

    private void CBdesayunodespuesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBdesayunodespuesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBdesayunodespuesItemStateChanged

    private void CBalmuerzoantesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBalmuerzoantesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBalmuerzoantesItemStateChanged

    private void CBalmuerzodespuesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBalmuerzodespuesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBalmuerzodespuesItemStateChanged

    private void CBcenaantesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBcenaantesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBcenaantesItemStateChanged

    private void CBcenadespuesItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBcenadespuesItemStateChanged
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBcenadespuesItemStateChanged

    private void CBdesayunoItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBdesayunoItemStateChanged
        CBdesayunoantes.setState(CBdesayuno.getState());
        CBdesayunodespues.setState(CBdesayuno.getState());
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBdesayunoItemStateChanged

    private void CBalmuerzoItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBalmuerzoItemStateChanged
        CBalmuerzoantes.setState(CBalmuerzo.getState());
        CBalmuerzodespues.setState(CBalmuerzo.getState());
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBalmuerzoItemStateChanged

    private void CBcenaItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_CBcenaItemStateChanged
        CBcenaantes.setState(CBcena.getState());
        CBcenadespues.setState(CBcena.getState());
        JFrame.getFrames()[0].repaint();
    }//GEN-LAST:event_CBcenaItemStateChanged

    public static void main(String args[]){
        java.awt.EventQueue.invokeLater(new Runnable(){
            public void run(){
                new csds60analyzerGUI().setVisible(true);
            }
        });
    }

    public void paint(Graphics g){
        if(grafica == null)
            grafica = this.creaImagen();
        g.drawImage(grafica,20,50,null);
        grafica=null;
        new FileDrop(JFrame.getFrames()[0],new FileDrop.Listener(){
            public void filesDropped(File[] arg0){
                System.out.println(arg0[0]);
                fichero=arg0[0].toString();
                JFrame.getFrames()[0].repaint();
            }
        });
    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private java.awt.Checkbox CBalmuerzo;
    private java.awt.Checkbox CBalmuerzoantes;
    private java.awt.Checkbox CBalmuerzodespues;
    private java.awt.Checkbox CBcena;
    private java.awt.Checkbox CBcenaantes;
    private java.awt.Checkbox CBcenadespues;
    private java.awt.Checkbox CBdesayuno;
    private java.awt.Checkbox CBdesayunoantes;
    private java.awt.Checkbox CBdesayunodespues;
    private java.awt.Label label1;
    private java.awt.PopupMenu popupMenu1;
    private java.awt.PopupMenu popupMenu2;
    // End of variables declaration//GEN-END:variables

}

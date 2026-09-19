package com.aprendiz.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name = "aprendiz")
public class AprendizEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "apellido")
    private String apellido;

    @Column(name = "email", unique = true)
    private String email;

    @Column(name = "telefono")
    private String telefono;

    @Column(name = "direccion")
    private String direccion;

    @Column(name = "documento", unique = true)
    private String documento;

    @Column(name = "tipo_documento")
    private String tipo_documento;

    @Column(name = "fecha_nacimiento")
    private String fecha_nacimiento;

    @Column(name = "programa_formacion")
    private String programa_formacion;

    @Column(name = "ficha")
    private String ficha;
}
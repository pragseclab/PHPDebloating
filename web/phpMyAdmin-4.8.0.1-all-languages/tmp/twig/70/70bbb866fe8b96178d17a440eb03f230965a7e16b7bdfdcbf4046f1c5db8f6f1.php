<?php

/* columns_definitions/column_attributes.twig */
class __TwigTemplate_5fa5b3a2c1eebcf3fc1212d24e89db279547687f837ea54b3e8f995dff1c61a9 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 2
        $context["ci"] = 0;
        // line 3
        echo "
";
        // line 6
        $context["ci_offset"] =  -1;
        // line 7
        echo "
<td class=\"center\">
    ";
        // line 10
        echo "    ";
        $this->loadTemplate("columns_definitions/column_name.twig", "columns_definitions/column_attributes.twig", 10)->display(array("column_number" =>         // line 11
($context["column_number"] ?? null), "ci" =>         // line 12
($context["ci"] ?? null), "ci_offset" =>         // line 13
($context["ci_offset"] ?? null), "column_meta" =>         // line 14
($context["column_meta"] ?? null), "cfg_relation" =>         // line 15
($context["cfg_relation"] ?? null), "max_rows" =>         // line 16
($context["max_rows"] ?? null)));
        // line 18
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 19
        echo "</td>
<td class=\"center\">
    ";
        // line 22
        echo "    ";
        $this->loadTemplate("columns_definitions/column_type.twig", "columns_definitions/column_attributes.twig", 22)->display(array("column_number" =>         // line 23
($context["column_number"] ?? null), "ci" =>         // line 24
($context["ci"] ?? null), "ci_offset" =>         // line 25
($context["ci_offset"] ?? null), "column_meta" =>         // line 26
($context["column_meta"] ?? null), "type_upper" =>         // line 27
($context["type_upper"] ?? null)));
        // line 29
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 30
        echo "</td>
<td class=\"center\">
    ";
        // line 33
        echo "    ";
        $this->loadTemplate("columns_definitions/column_length.twig", "columns_definitions/column_attributes.twig", 33)->display(array("column_number" =>         // line 34
($context["column_number"] ?? null), "ci" =>         // line 35
($context["ci"] ?? null), "ci_offset" =>         // line 36
($context["ci_offset"] ?? null), "length_values_input_size" =>         // line 37
($context["length_values_input_size"] ?? null), "length_to_display" =>         // line 38
($context["length"] ?? null)));
        // line 40
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 41
        echo "</td>
<td class=\"center\">
    ";
        // line 44
        echo "    ";
        $this->loadTemplate("columns_definitions/column_default.twig", "columns_definitions/column_attributes.twig", 44)->display(array("column_number" =>         // line 45
($context["column_number"] ?? null), "ci" =>         // line 46
($context["ci"] ?? null), "ci_offset" =>         // line 47
($context["ci_offset"] ?? null), "column_meta" =>         // line 48
($context["column_meta"] ?? null), "type_upper" =>         // line 49
($context["type_upper"] ?? null), "char_editing" =>         // line 50
($context["char_editing"] ?? null)));
        // line 52
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 53
        echo "</td>
<td class=\"center\">
    ";
        // line 56
        echo "    ";
        echo PhpMyAdmin\Charsets::getCollationDropdownBox(        // line 57
($context["dbi"] ?? null),         // line 58
($context["disable_is"] ?? null), (("field_collation[" .         // line 59
($context["column_number"] ?? null)) . "]"), ((("field_" .         // line 60
($context["column_number"] ?? null)) . "_") . (($context["ci"] ?? null) - ($context["ci_offset"] ?? null))), (( !twig_test_empty($this->getAttribute(        // line 61
($context["column_meta"] ?? null), "Collation", array(), "array"))) ? ($this->getAttribute(($context["column_meta"] ?? null), "Collation", array(), "array")) : (null)), false);
        // line 63
        echo "
</td>
<td class=\"center\">
    ";
        // line 67
        echo "    ";
        $this->loadTemplate("columns_definitions/column_attribute.twig", "columns_definitions/column_attributes.twig", 67)->display(array("column_number" =>         // line 68
($context["column_number"] ?? null), "ci" =>         // line 69
($context["ci"] ?? null), "ci_offset" =>         // line 70
($context["ci_offset"] ?? null), "column_meta" =>         // line 71
($context["column_meta"] ?? null), "extracted_columnspec" =>         // line 72
($context["extracted_columnspec"] ?? null), "submit_attribute" =>         // line 73
($context["submit_attribute"] ?? null), "attribute_types" =>         // line 74
($context["attribute_types"] ?? null)));
        // line 76
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 77
        echo "</td>
<td class=\"center\">
    ";
        // line 80
        echo "    ";
        $this->loadTemplate("columns_definitions/column_null.twig", "columns_definitions/column_attributes.twig", 80)->display(array("column_number" =>         // line 81
($context["column_number"] ?? null), "ci" =>         // line 82
($context["ci"] ?? null), "ci_offset" =>         // line 83
($context["ci_offset"] ?? null), "column_meta" =>         // line 84
($context["column_meta"] ?? null)));
        // line 86
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 87
        echo "</td>
";
        // line 88
        if ((array_key_exists("change_column", $context) &&  !twig_test_empty(($context["change_column"] ?? null)))) {
            // line 89
            echo "    ";
            // line 90
            echo "    <td class=\"center\">
        ";
            // line 91
            $this->loadTemplate("columns_definitions/column_adjust_privileges.twig", "columns_definitions/column_attributes.twig", 91)->display(array("column_number" =>             // line 92
($context["column_number"] ?? null), "ci" =>             // line 93
($context["ci"] ?? null), "ci_offset" =>             // line 94
($context["ci_offset"] ?? null), "privs_available" =>             // line 95
($context["privs_available"] ?? null)));
            // line 97
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 98
            echo "    </td>
";
        }
        // line 100
        if ( !($context["is_backup"] ?? null)) {
            // line 101
            echo "    ";
            // line 102
            echo "    <td class=\"center\">
        ";
            // line 103
            $this->loadTemplate("columns_definitions/column_indexes.twig", "columns_definitions/column_attributes.twig", 103)->display(array("column_number" =>             // line 104
($context["column_number"] ?? null), "ci" =>             // line 105
($context["ci"] ?? null), "ci_offset" =>             // line 106
($context["ci_offset"] ?? null), "column_meta" =>             // line 107
($context["column_meta"] ?? null)));
            // line 109
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 110
            echo "    </td>
";
        }
        // line 112
        echo "<td class=\"center\">
    ";
        // line 114
        echo "    ";
        $this->loadTemplate("columns_definitions/column_auto_increment.twig", "columns_definitions/column_attributes.twig", 114)->display(array("column_number" =>         // line 115
($context["column_number"] ?? null), "ci" =>         // line 116
($context["ci"] ?? null), "ci_offset" =>         // line 117
($context["ci_offset"] ?? null), "column_meta" =>         // line 118
($context["column_meta"] ?? null)));
        // line 120
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 121
        echo "</td>
<td class=\"center\">
    ";
        // line 124
        echo "    ";
        $this->loadTemplate("columns_definitions/column_comment.twig", "columns_definitions/column_attributes.twig", 124)->display(array("column_number" =>         // line 125
($context["column_number"] ?? null), "ci" =>         // line 126
($context["ci"] ?? null), "ci_offset" =>         // line 127
($context["ci_offset"] ?? null), "max_length" =>         // line 128
($context["max_length"] ?? null), "value" => (((($this->getAttribute(        // line 129
($context["column_meta"] ?? null), "Field", array(), "array", true, true) && twig_test_iterable(        // line 130
($context["comments_map"] ?? null))) && $this->getAttribute(        // line 131
($context["comments_map"] ?? null), $this->getAttribute(($context["column_meta"] ?? null), "Field", array(), "array"), array(), "array", true, true))) ? (twig_escape_filter($this->env, $this->getAttribute(        // line 132
($context["comments_map"] ?? null), $this->getAttribute(($context["column_meta"] ?? null), "Field", array(), "array"), array(), "array"))) : (""))));
        // line 134
        echo "    ";
        $context["ci"] = (($context["ci"] ?? null) + 1);
        // line 135
        echo "</td>
 ";
        // line 137
        if (($context["is_virtual_columns_supported"] ?? null)) {
            // line 138
            echo "    <td class=\"center\">
        ";
            // line 139
            $this->loadTemplate("columns_definitions/column_virtuality.twig", "columns_definitions/column_attributes.twig", 139)->display(array("column_number" =>             // line 140
($context["column_number"] ?? null), "ci" =>             // line 141
($context["ci"] ?? null), "ci_offset" =>             // line 142
($context["ci_offset"] ?? null), "column_meta" =>             // line 143
($context["column_meta"] ?? null), "char_editing" =>             // line 144
($context["char_editing"] ?? null), "expression" => (($this->getAttribute(            // line 145
($context["column_meta"] ?? null), "Expression", array(), "array", true, true)) ? ($this->getAttribute(($context["column_meta"] ?? null), "Expression", array(), "array")) : ("")), "options" =>             // line 146
($context["options"] ?? null)));
            // line 148
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 149
            echo "    </td>
";
        }
        // line 152
        if (array_key_exists("fields_meta", $context)) {
            // line 153
            echo "    ";
            $context["current_index"] = 0;
            // line 154
            echo "    ";
            $context["cols"] = (twig_length_filter($this->env, ($context["move_columns"] ?? null)) - 1);
            // line 155
            echo "    ";
            $context["break"] = false;
            // line 156
            echo "    ";
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable(range(0, ($context["cols"] ?? null)));
            foreach ($context['_seq'] as $context["_key"] => $context["mi"]) {
                if ((($this->getAttribute($this->getAttribute(($context["move_columns"] ?? null), $context["mi"], array(), "array"), "name", array()) == $this->getAttribute(($context["column_meta"] ?? null), "Field", array(), "array")) &&  !($context["break"] ?? null))) {
                    // line 157
                    echo "        ";
                    $context["current_index"] = $context["mi"];
                    // line 158
                    echo "        ";
                    $context["break"] = true;
                    // line 159
                    echo "    ";
                }
            }
            $_parent = $context['_parent'];
            unset($context['_seq'], $context['_iterated'], $context['_key'], $context['mi'], $context['_parent'], $context['loop']);
            $context = array_intersect_key($context, $_parent) + $_parent;
            // line 160
            echo "
    <td class=\"center\">
        ";
            // line 162
            $this->loadTemplate("columns_definitions/move_column.twig", "columns_definitions/column_attributes.twig", 162)->display(array("column_number" =>             // line 163
($context["column_number"] ?? null), "ci" =>             // line 164
($context["ci"] ?? null), "ci_offset" =>             // line 165
($context["ci_offset"] ?? null), "column_meta" =>             // line 166
($context["column_meta"] ?? null), "move_columns" =>             // line 167
($context["move_columns"] ?? null), "current_index" =>             // line 168
($context["current_index"] ?? null)));
            // line 170
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 171
            echo "    </td>
";
        }
        // line 173
        echo "
";
        // line 174
        if ((($this->getAttribute(($context["cfg_relation"] ?? null), "mimework", array(), "array") && ($context["browse_mime"] ?? null)) && $this->getAttribute(($context["cfg_relation"] ?? null), "commwork", array(), "array"))) {
            // line 175
            echo "    <td class=\"center\">
        ";
            // line 177
            echo "        ";
            $this->loadTemplate("columns_definitions/mime_type.twig", "columns_definitions/column_attributes.twig", 177)->display(array("column_number" =>             // line 178
($context["column_number"] ?? null), "ci" =>             // line 179
($context["ci"] ?? null), "ci_offset" =>             // line 180
($context["ci_offset"] ?? null), "column_meta" =>             // line 181
($context["column_meta"] ?? null), "available_mime" =>             // line 182
($context["available_mime"] ?? null), "mime_map" =>             // line 183
($context["mime_map"] ?? null)));
            // line 185
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 186
            echo "    </td>
    <td class=\"center\">
        ";
            // line 189
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation.twig", "columns_definitions/column_attributes.twig", 189)->display(array("column_number" =>             // line 190
($context["column_number"] ?? null), "ci" =>             // line 191
($context["ci"] ?? null), "ci_offset" =>             // line 192
($context["ci_offset"] ?? null), "column_meta" =>             // line 193
($context["column_meta"] ?? null), "available_mime" =>             // line 194
($context["available_mime"] ?? null), "mime_map" =>             // line 195
($context["mime_map"] ?? null), "type" => "transformation"));
            // line 198
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 199
            echo "    </td>
    <td class=\"center\">
        ";
            // line 202
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation_option.twig", "columns_definitions/column_attributes.twig", 202)->display(array("column_number" =>             // line 203
($context["column_number"] ?? null), "ci" =>             // line 204
($context["ci"] ?? null), "ci_offset" =>             // line 205
($context["ci_offset"] ?? null), "column_meta" =>             // line 206
($context["column_meta"] ?? null), "mime_map" =>             // line 207
($context["mime_map"] ?? null), "type_prefix" => ""));
            // line 210
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 211
            echo "    </td>
    <td class=\"center\">
        ";
            // line 214
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation.twig", "columns_definitions/column_attributes.twig", 214)->display(array("column_number" =>             // line 215
($context["column_number"] ?? null), "ci" =>             // line 216
($context["ci"] ?? null), "ci_offset" =>             // line 217
($context["ci_offset"] ?? null), "column_meta" =>             // line 218
($context["column_meta"] ?? null), "available_mime" =>             // line 219
($context["available_mime"] ?? null), "mime_map" =>             // line 220
($context["mime_map"] ?? null), "type" => "input_transformation"));
            // line 223
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 224
            echo "    </td>
    <td class=\"center\">
        ";
            // line 227
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation_option.twig", "columns_definitions/column_attributes.twig", 227)->display(array("column_number" =>             // line 228
($context["column_number"] ?? null), "ci" =>             // line 229
($context["ci"] ?? null), "ci_offset" =>             // line 230
($context["ci_offset"] ?? null), "column_meta" =>             // line 231
($context["column_meta"] ?? null), "mime_map" =>             // line 232
($context["mime_map"] ?? null), "type_prefix" => "input_"));
            // line 235
            echo "        ";
            $context["ci"] = (($context["ci"] ?? null) + 1);
            // line 236
            echo "    </td>
";
        }
    }

    public function getTemplateName()
    {
        return "columns_definitions/column_attributes.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  361 => 236,  358 => 235,  356 => 232,  355 => 231,  354 => 230,  353 => 229,  352 => 228,  350 => 227,  346 => 224,  343 => 223,  341 => 220,  340 => 219,  339 => 218,  338 => 217,  337 => 216,  336 => 215,  334 => 214,  330 => 211,  327 => 210,  325 => 207,  324 => 206,  323 => 205,  322 => 204,  321 => 203,  319 => 202,  315 => 199,  312 => 198,  310 => 195,  309 => 194,  308 => 193,  307 => 192,  306 => 191,  305 => 190,  303 => 189,  299 => 186,  296 => 185,  294 => 183,  293 => 182,  292 => 181,  291 => 180,  290 => 179,  289 => 178,  287 => 177,  284 => 175,  282 => 174,  279 => 173,  275 => 171,  272 => 170,  270 => 168,  269 => 167,  268 => 166,  267 => 165,  266 => 164,  265 => 163,  264 => 162,  260 => 160,  253 => 159,  250 => 158,  247 => 157,  241 => 156,  238 => 155,  235 => 154,  232 => 153,  230 => 152,  226 => 149,  223 => 148,  221 => 146,  220 => 145,  219 => 144,  218 => 143,  217 => 142,  216 => 141,  215 => 140,  214 => 139,  211 => 138,  209 => 137,  206 => 135,  203 => 134,  201 => 132,  200 => 131,  199 => 130,  198 => 129,  197 => 128,  196 => 127,  195 => 126,  194 => 125,  192 => 124,  188 => 121,  185 => 120,  183 => 118,  182 => 117,  181 => 116,  180 => 115,  178 => 114,  175 => 112,  171 => 110,  168 => 109,  166 => 107,  165 => 106,  164 => 105,  163 => 104,  162 => 103,  159 => 102,  157 => 101,  155 => 100,  151 => 98,  148 => 97,  146 => 95,  145 => 94,  144 => 93,  143 => 92,  142 => 91,  139 => 90,  137 => 89,  135 => 88,  132 => 87,  129 => 86,  127 => 84,  126 => 83,  125 => 82,  124 => 81,  122 => 80,  118 => 77,  115 => 76,  113 => 74,  112 => 73,  111 => 72,  110 => 71,  109 => 70,  108 => 69,  107 => 68,  105 => 67,  100 => 63,  98 => 61,  97 => 60,  96 => 59,  95 => 58,  94 => 57,  92 => 56,  88 => 53,  85 => 52,  83 => 50,  82 => 49,  81 => 48,  80 => 47,  79 => 46,  78 => 45,  76 => 44,  72 => 41,  69 => 40,  67 => 38,  66 => 37,  65 => 36,  64 => 35,  63 => 34,  61 => 33,  57 => 30,  54 => 29,  52 => 27,  51 => 26,  50 => 25,  49 => 24,  48 => 23,  46 => 22,  42 => 19,  39 => 18,  37 => 16,  36 => 15,  35 => 14,  34 => 13,  33 => 12,  32 => 11,  30 => 10,  26 => 7,  24 => 6,  21 => 3,  19 => 2,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "columns_definitions/column_attributes.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/columns_definitions/column_attributes.twig");
    }
}

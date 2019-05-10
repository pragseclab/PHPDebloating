<?php

/* columns_definitions/column_attributes.twig */
class __TwigTemplate_de25c6544d30bfe9e9cabe82cbe856cf98222ae47678e0d35353488874c8a364 extends Twig_Template
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
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 12
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 13
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 14
(isset($context["column_meta"]) ? $context["column_meta"] : null), "cfg_relation" =>         // line 15
(isset($context["cfg_relation"]) ? $context["cfg_relation"] : null), "max_rows" =>         // line 16
(isset($context["max_rows"]) ? $context["max_rows"] : null)));
        // line 18
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 19
        echo "</td>
<td class=\"center\">
    ";
        // line 22
        echo "    ";
        $this->loadTemplate("columns_definitions/column_type.twig", "columns_definitions/column_attributes.twig", 22)->display(array("column_number" =>         // line 23
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 24
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 25
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 26
(isset($context["column_meta"]) ? $context["column_meta"] : null), "type_upper" =>         // line 27
(isset($context["type_upper"]) ? $context["type_upper"] : null)));
        // line 29
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 30
        echo "</td>
<td class=\"center\">
    ";
        // line 33
        echo "    ";
        $this->loadTemplate("columns_definitions/column_length.twig", "columns_definitions/column_attributes.twig", 33)->display(array("column_number" =>         // line 34
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 35
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 36
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "length_values_input_size" =>         // line 37
(isset($context["length_values_input_size"]) ? $context["length_values_input_size"] : null), "length_to_display" =>         // line 38
(isset($context["length"]) ? $context["length"] : null)));
        // line 40
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 41
        echo "</td>
<td class=\"center\">
    ";
        // line 44
        echo "    ";
        $this->loadTemplate("columns_definitions/column_default.twig", "columns_definitions/column_attributes.twig", 44)->display(array("column_number" =>         // line 45
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 46
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 47
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 48
(isset($context["column_meta"]) ? $context["column_meta"] : null), "type_upper" =>         // line 49
(isset($context["type_upper"]) ? $context["type_upper"] : null), "char_editing" =>         // line 50
(isset($context["char_editing"]) ? $context["char_editing"] : null)));
        // line 52
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 53
        echo "</td>
<td class=\"center\">
    ";
        // line 56
        echo "    ";
        echo PhpMyAdmin\Charsets::getCollationDropdownBox(        // line 57
(isset($context["dbi"]) ? $context["dbi"] : null),         // line 58
(isset($context["disable_is"]) ? $context["disable_is"] : null), (("field_collation[" .         // line 59
(isset($context["column_number"]) ? $context["column_number"] : null)) . "]"), ((("field_" .         // line 60
(isset($context["column_number"]) ? $context["column_number"] : null)) . "_") . ((isset($context["ci"]) ? $context["ci"] : null) - (isset($context["ci_offset"]) ? $context["ci_offset"] : null))), (( !twig_test_empty($this->getAttribute(        // line 61
(isset($context["column_meta"]) ? $context["column_meta"] : null), "Collation", array(), "array"))) ? ($this->getAttribute((isset($context["column_meta"]) ? $context["column_meta"] : null), "Collation", array(), "array")) : (null)), false);
        // line 63
        echo "
</td>
<td class=\"center\">
    ";
        // line 67
        echo "    ";
        $this->loadTemplate("columns_definitions/column_attribute.twig", "columns_definitions/column_attributes.twig", 67)->display(array("column_number" =>         // line 68
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 69
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 70
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 71
(isset($context["column_meta"]) ? $context["column_meta"] : null), "extracted_columnspec" =>         // line 72
(isset($context["extracted_columnspec"]) ? $context["extracted_columnspec"] : null), "submit_attribute" =>         // line 73
(isset($context["submit_attribute"]) ? $context["submit_attribute"] : null), "attribute_types" =>         // line 74
(isset($context["attribute_types"]) ? $context["attribute_types"] : null)));
        // line 76
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 77
        echo "</td>
<td class=\"center\">
    ";
        // line 80
        echo "    ";
        $this->loadTemplate("columns_definitions/column_null.twig", "columns_definitions/column_attributes.twig", 80)->display(array("column_number" =>         // line 81
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 82
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 83
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 84
(isset($context["column_meta"]) ? $context["column_meta"] : null)));
        // line 86
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 87
        echo "</td>
";
        // line 88
        if ((array_key_exists("change_column", $context) &&  !twig_test_empty((isset($context["change_column"]) ? $context["change_column"] : null)))) {
            // line 89
            echo "    ";
            // line 90
            echo "    <td class=\"center\">
        ";
            // line 91
            $this->loadTemplate("columns_definitions/column_adjust_privileges.twig", "columns_definitions/column_attributes.twig", 91)->display(array("column_number" =>             // line 92
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 93
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 94
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "privs_available" =>             // line 95
(isset($context["privs_available"]) ? $context["privs_available"] : null)));
            // line 97
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 98
            echo "    </td>
";
        }
        // line 100
        if ( !(isset($context["is_backup"]) ? $context["is_backup"] : null)) {
            // line 101
            echo "    ";
            // line 102
            echo "    <td class=\"center\">
        ";
            // line 103
            $this->loadTemplate("columns_definitions/column_indexes.twig", "columns_definitions/column_attributes.twig", 103)->display(array("column_number" =>             // line 104
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 105
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 106
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 107
(isset($context["column_meta"]) ? $context["column_meta"] : null)));
            // line 109
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
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
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 116
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 117
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>         // line 118
(isset($context["column_meta"]) ? $context["column_meta"] : null)));
        // line 120
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 121
        echo "</td>
<td class=\"center\">
    ";
        // line 124
        echo "    ";
        $this->loadTemplate("columns_definitions/column_comment.twig", "columns_definitions/column_attributes.twig", 124)->display(array("column_number" =>         // line 125
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>         // line 126
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>         // line 127
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "max_length" =>         // line 128
(isset($context["max_length"]) ? $context["max_length"] : null), "value" => (((($this->getAttribute(        // line 129
(isset($context["column_meta"]) ? $context["column_meta"] : null), "Field", array(), "array", true, true) && twig_test_iterable(        // line 130
(isset($context["comments_map"]) ? $context["comments_map"] : null))) && $this->getAttribute(        // line 131
(isset($context["comments_map"]) ? $context["comments_map"] : null), $this->getAttribute((isset($context["column_meta"]) ? $context["column_meta"] : null), "Field", array(), "array"), array(), "array", true, true))) ? (twig_escape_filter($this->env, $this->getAttribute(        // line 132
(isset($context["comments_map"]) ? $context["comments_map"] : null), $this->getAttribute((isset($context["column_meta"]) ? $context["column_meta"] : null), "Field", array(), "array"), array(), "array"))) : (""))));
        // line 134
        echo "    ";
        $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
        // line 135
        echo "</td>
 ";
        // line 137
        if ((isset($context["is_virtual_columns_supported"]) ? $context["is_virtual_columns_supported"] : null)) {
            // line 138
            echo "    <td class=\"center\">
        ";
            // line 139
            $this->loadTemplate("columns_definitions/column_virtuality.twig", "columns_definitions/column_attributes.twig", 139)->display(array("column_number" =>             // line 140
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 141
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 142
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 143
(isset($context["column_meta"]) ? $context["column_meta"] : null), "char_editing" =>             // line 144
(isset($context["char_editing"]) ? $context["char_editing"] : null), "expression" => (($this->getAttribute(            // line 145
(isset($context["column_meta"]) ? $context["column_meta"] : null), "Expression", array(), "array", true, true)) ? ($this->getAttribute((isset($context["column_meta"]) ? $context["column_meta"] : null), "Expression", array(), "array")) : ("")), "options" =>             // line 146
(isset($context["options"]) ? $context["options"] : null)));
            // line 148
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
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
            $context["cols"] = (twig_length_filter($this->env, (isset($context["move_columns"]) ? $context["move_columns"] : null)) - 1);
            // line 155
            echo "    ";
            $context["break"] = false;
            // line 156
            echo "    ";
            $context['_parent'] = $context;
            $context['_seq'] = twig_ensure_traversable(range(0, (isset($context["cols"]) ? $context["cols"] : null)));
            foreach ($context['_seq'] as $context["_key"] => $context["mi"]) {
                if ((($this->getAttribute($this->getAttribute((isset($context["move_columns"]) ? $context["move_columns"] : null), $context["mi"], array(), "array"), "name", array()) == $this->getAttribute((isset($context["column_meta"]) ? $context["column_meta"] : null), "Field", array(), "array")) &&  !(isset($context["break"]) ? $context["break"] : null))) {
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
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 164
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 165
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 166
(isset($context["column_meta"]) ? $context["column_meta"] : null), "move_columns" =>             // line 167
(isset($context["move_columns"]) ? $context["move_columns"] : null), "current_index" =>             // line 168
(isset($context["current_index"]) ? $context["current_index"] : null)));
            // line 170
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 171
            echo "    </td>
";
        }
        // line 173
        echo "
";
        // line 174
        if ((($this->getAttribute((isset($context["cfg_relation"]) ? $context["cfg_relation"] : null), "mimework", array(), "array") && (isset($context["browse_mime"]) ? $context["browse_mime"] : null)) && $this->getAttribute((isset($context["cfg_relation"]) ? $context["cfg_relation"] : null), "commwork", array(), "array"))) {
            // line 175
            echo "    <td class=\"center\">
        ";
            // line 177
            echo "        ";
            $this->loadTemplate("columns_definitions/mime_type.twig", "columns_definitions/column_attributes.twig", 177)->display(array("column_number" =>             // line 178
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 179
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 180
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 181
(isset($context["column_meta"]) ? $context["column_meta"] : null), "available_mime" =>             // line 182
(isset($context["available_mime"]) ? $context["available_mime"] : null), "mime_map" =>             // line 183
(isset($context["mime_map"]) ? $context["mime_map"] : null)));
            // line 185
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 186
            echo "    </td>
    <td class=\"center\">
        ";
            // line 189
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation.twig", "columns_definitions/column_attributes.twig", 189)->display(array("column_number" =>             // line 190
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 191
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 192
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 193
(isset($context["column_meta"]) ? $context["column_meta"] : null), "available_mime" =>             // line 194
(isset($context["available_mime"]) ? $context["available_mime"] : null), "mime_map" =>             // line 195
(isset($context["mime_map"]) ? $context["mime_map"] : null), "type" => "transformation"));
            // line 198
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 199
            echo "    </td>
    <td class=\"center\">
        ";
            // line 202
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation_option.twig", "columns_definitions/column_attributes.twig", 202)->display(array("column_number" =>             // line 203
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 204
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 205
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 206
(isset($context["column_meta"]) ? $context["column_meta"] : null), "mime_map" =>             // line 207
(isset($context["mime_map"]) ? $context["mime_map"] : null), "type_prefix" => ""));
            // line 210
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 211
            echo "    </td>
    <td class=\"center\">
        ";
            // line 214
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation.twig", "columns_definitions/column_attributes.twig", 214)->display(array("column_number" =>             // line 215
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 216
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 217
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 218
(isset($context["column_meta"]) ? $context["column_meta"] : null), "available_mime" =>             // line 219
(isset($context["available_mime"]) ? $context["available_mime"] : null), "mime_map" =>             // line 220
(isset($context["mime_map"]) ? $context["mime_map"] : null), "type" => "input_transformation"));
            // line 223
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
            // line 224
            echo "    </td>
    <td class=\"center\">
        ";
            // line 227
            echo "        ";
            $this->loadTemplate("columns_definitions/transformation_option.twig", "columns_definitions/column_attributes.twig", 227)->display(array("column_number" =>             // line 228
(isset($context["column_number"]) ? $context["column_number"] : null), "ci" =>             // line 229
(isset($context["ci"]) ? $context["ci"] : null), "ci_offset" =>             // line 230
(isset($context["ci_offset"]) ? $context["ci_offset"] : null), "column_meta" =>             // line 231
(isset($context["column_meta"]) ? $context["column_meta"] : null), "mime_map" =>             // line 232
(isset($context["mime_map"]) ? $context["mime_map"] : null), "type_prefix" => "input_"));
            // line 235
            echo "        ";
            $context["ci"] = ((isset($context["ci"]) ? $context["ci"] : null) + 1);
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
